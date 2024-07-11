import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to fetch stock data
def fetch_stock_data(symbols):
    data = {}
    for symbol in symbols:
        ticker = f"{symbol}.NS"
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period="1d")
        if not stock_data.empty:
            data[symbol] = stock_data['Close'].values[0]
        else:
            data[symbol] = None
    return data

st.title("Indian Stock Prices Fetcher")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    stock_symbols = df.iloc[:, 0].tolist()  # Read the first column ignoring the header
    
    if st.button("Fetch Latest Stock Prices"):
        stock_data = fetch_stock_data(stock_symbols)
        result_df = pd.DataFrame(stock_data.items(), columns=['Instrument', 'Latest Value'])
        
        st.write("## Stock Prices")
        st.dataframe(result_df)

        # Generate CSV
        csv = result_df.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='latest_stock_prices.csv',
            mime='text/csv',
        )

        # Visualizations
        st.write("## Visualizations")

        # Bar plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='Latest Value', y='Instrument', data=result_df, ax=ax)
        ax.set_title('Stock Prices')
        st.pyplot(fig)

        # Distribution plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(result_df['Latest Value'].dropna(), kde=True, ax=ax)
        ax.set_title('Distribution of Stock Prices')
        st.pyplot(fig)

        # Box plot of stock prices
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='Latest Value', data=result_df, ax=ax)
        ax.set_title('Box Plot of Stock Prices')
        st.pyplot(fig)
