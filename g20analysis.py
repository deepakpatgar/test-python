import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the CSV data
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv("G20-CNTRY.csv", encoding="latin1")  # Specify the encoding here

    # Convert the numeric columns to numeric
    numeric_columns = ["Trade", "Nom_GDP", "PPP_GDP", "Nom_GDP_per_capita", "PPP_GDP_per_capita", "HDI", "Population", "Area"]
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    return data

# Create a Streamlit app
def main():
    st.title("G20 Country Data Analysis")

    # Load the data
    data = load_data()

    # Display the raw data
    st.subheader("Raw Data")
    st.dataframe(data)

    # Select columns for analysis
    selected_columns = st.multiselect("Select columns for analysis:", data.columns)

    # Define numeric columns here
    numeric_columns = ["Trade", "Nom_GDP", "PPP_GDP", "Nom_GDP_per_capita", "PPP_GDP_per_capita", "HDI", "Population", "Area"]

    # Handle string and numeric columns separately
    string_columns = [col for col in selected_columns if col not in numeric_columns]

    # Convert selected numeric columns to numeric while handling NaN values
    numeric_data = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

    # Handle NaN values for numeric data
    numeric_data = numeric_data.dropna()  # This will remove rows with NaN values

    # Sidebar for interaction
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select Chart Type:", ["Bar Chart", "Multi Bar Chart", "Histogram", "Line Chart", "Box Plot", "Scatter Plot", "Heatmap", "Count Plot", "Pie Chart", "Numeric Correlation Heatmap", "Pair Plot"])
    selected_column = st.sidebar.selectbox("Select Column for Visualization:", selected_columns)
    slider_min = None
    slider_max = None
    slider_value = None
    if selected_column in numeric_columns:
        slider_min = int(numeric_data[selected_column].min(skipna=True))
        slider_max = int(numeric_data[selected_column].max())
        slider_value = st.sidebar.slider(f"Select {selected_column} Range:", slider_min, slider_max, (slider_min, slider_max))

    # Filter data based on slider range (only for numeric columns)
    if selected_column in numeric_columns:
        filtered_data = numeric_data[(numeric_data[selected_column] >= slider_value[0]) & (numeric_data[selected_column] <= slider_value[1])]
    else:
        filtered_data = data

    # Data visualization
    st.header("Data Visualization")

    if chart_type == "Bar Chart":
        st.subheader(f"Bar Chart for {selected_column} grouped by a string column")
        string_column = st.sidebar.selectbox("Select a String Column for Grouping:", string_columns)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=filtered_data, x=string_column, y=selected_column)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif chart_type == "Multi Bar Chart":
        st.subheader(f"Multi Bar Chart for selected columns")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=filtered_data, ci=None)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif chart_type == "Histogram" and selected_column in numeric_columns:
        st.subheader(f"Histogram for {selected_column}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(filtered_data[selected_column], kde=True)
        st.pyplot(fig)

    elif chart_type == "Line Chart" and selected_column in numeric_columns:
        st.subheader(f"Line Chart for {selected_column}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=filtered_data.index, y=filtered_data[selected_column])
        plt.xticks(rotation=90)
        st.pyplot(fig)

    elif chart_type == "Box Plot" and selected_column in numeric_columns:
        st.subheader(f"Box Plot for {selected_column}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(y=filtered_data[selected_column])
        st.pyplot(fig)

    elif chart_type == "Scatter Plot" and len(selected_columns) == 2:
        st.subheader(f"Scatter Plot for {selected_columns[0]} vs {selected_columns[1]}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=filtered_data, x=selected_columns[0], y=selected_columns[1])
        st.pyplot(fig)

    elif chart_type == "Heatmap" and len(selected_columns) >= 2:
        st.subheader(f"Heatmap for selected columns")
        correlation_matrix = filtered_data[selected_columns].corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        st.pyplot(fig)

    elif chart_type == "Count Plot" and selected_column in string_columns:
        st.subheader(f"Count Plot for {selected_column}")
        value_counts = filtered_data[selected_column].value_counts()
        st.bar_chart(value_counts)

    elif chart_type == "Pie Chart" and selected_column in string_columns:
        st.subheader(f"Pie Chart for {selected_column}")
        pie_data = filtered_data[selected_column].value_counts()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)

    elif chart_type == "Numeric Correlation Heatmap":
        st.subheader(f"Correlation Heatmap for Numeric Columns")
        correlation_matrix = numeric_data.corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        st.pyplot(fig)

    elif chart_type == "Pair Plot" and len(numeric_columns) >= 2:
        st.subheader(f"Pair Plot for Numeric Columns")
        pair_plot_data = filtered_data[numeric_columns]
        pair_plot = sns.pairplot(pair_plot_data)
        st.pyplot(pair_plot)

if __name__ == "__main__":
    main()




