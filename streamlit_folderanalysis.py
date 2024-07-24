import streamlit as st
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Function to get folder statistics
def get_folder_stats(folder_path):
    file_data = []
    subfolders = []
    file_formats = {}
    inaccessible_paths = []

    for root, dirs, files in os.walk(folder_path):
        # Track subfolders
        for d in dirs:
            subfolder_path = os.path.join(root, d)
            if os.path.isdir(subfolder_path):
                subfolders.append(subfolder_path)

        # Track files
        for file in files:
            file_path = os.path.join(root, file)
            try:
                stats = os.stat(file_path)
                creation_time = datetime.datetime.fromtimestamp(stats.st_ctime)
                modified_time = datetime.datetime.fromtimestamp(stats.st_mtime)
                size = stats.st_size
                file_format = file.split('.')[-1] if '.' in file else 'Unknown'

                file_data.append({
                    'File Name': file,
                    'File Path': file_path,
                    'File Size (Bytes)': size,
                    'Creation Date': creation_time,
                    'Modified Date': modified_time,
                    'File Format': file_format
                })

                if file_format in file_formats:
                    file_formats[file_format] += 1
                else:
                    file_formats[file_format] = 1
            except (FileNotFoundError, PermissionError) as e:
                # Handle inaccessible files
                inaccessible_paths.append(file_path)

    df = pd.DataFrame(file_data)
    return df, len(subfolders), len(file_data), file_formats, inaccessible_paths

# Streamlit App
st.title("Folder Statistics Analyzer")

# Upload Folder
folder = st.text_input("Enter the folder path:")

if folder:
    if os.path.exists(folder):
        # Get folder statistics
        df, num_subfolders, num_files, file_formats, inaccessible_paths = get_folder_stats(folder)
        
        # Display statistics
        st.write(f"Number of Subfolders: {num_subfolders}")
        st.write(f"Number of Files: {num_files}")
        st.write("File Formats Count:")
        st.write(file_formats)
        
        if inaccessible_paths:
            st.write("Inaccessible Files/Directories:")
            st.write(inaccessible_paths)
        
        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="folder_statistics.csv",
            mime="text/csv"
        )
        
        # Visualization
        st.subheader("File Size Distribution")
        plt.figure(figsize=(10, 6))
        sns.histplot(df['File Size (Bytes)'], kde=True)
        plt.title("File Size Distribution")
        plt.xlabel("File Size (Bytes)")
        plt.ylabel("Frequency")
        st.pyplot(plt.gcf())
        
        st.subheader("File Format Distribution")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(file_formats.keys()), y=list(file_formats.values()))
        plt.title("File Format Distribution")
        plt.xlabel("File Format")
        plt.ylabel("Count")
        st.pyplot(plt.gcf())
        
        st.subheader("File Size by Format")
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='File Format', y='File Size (Bytes)', data=df)
        plt.title("File Size Distribution by Format")
        plt.xlabel("File Format")
        plt.ylabel("File Size (Bytes)")
        plt.xticks(rotation=45)
        st.pyplot(plt.gcf())
        
        st.subheader("Number of Files by Format")
        plt.figure(figsize=(10, 6))
        labels = list(file_formats.keys())
        sizes = list(file_formats.values())
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Number of Files by Format")
        st.pyplot(plt.gcf())
        
        st.subheader("File Size Statistics")
        size_stats = df['File Size (Bytes)'].describe()
        stats_df = pd.DataFrame({
            'Statistic': ['Mean', 'Median', 'Std Dev'],
            'Value': [size_stats['mean'], size_stats['50%'], size_stats['std']]
        })
        st.write(stats_df)
        
        # Visualizations Side by Side
        st.subheader("File Changes Over Time")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("File Creation Over Time")
            plt.figure(figsize=(12, 6))
            df['Creation Date'] = pd.to_datetime(df['Creation Date'])
            creation_counts = df.resample('M', on='Creation Date').size()
            creation_counts.plot(kind='line')
            plt.title("Number of Files Created Per Month")
            plt.xlabel("Date")
            plt.ylabel("Number of Files")
            st.pyplot(plt.gcf())
        
        with col2:
            st.subheader("File Modification Over Time")
            plt.figure(figsize=(12, 6))
            df['Modified Date'] = pd.to_datetime(df['Modified Date'])
            modification_counts = df.resample('M', on='Modified Date').size()
            modification_counts.plot(kind='line', color='orange')
            plt.title("Number of Files Modified Per Month")
            plt.xlabel("Date")
            plt.ylabel("Number of Files")
            st.pyplot(plt.gcf())
        
        st.subheader("File Size by Creation Month")
        plt.figure(figsize=(12, 8))
        df['Creation Month'] = df['Creation Date'].dt.to_period('M')
        sns.boxplot(x='Creation Month', y='File Size (Bytes)', data=df)
        plt.title("File Size Distribution by Creation Month")
        plt.xlabel("Creation Month")
        plt.ylabel("File Size (Bytes)")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())
        
        st.subheader("File Size by Modification Month")
        plt.figure(figsize=(12, 8))
        df['Modification Month'] = df['Modified Date'].dt.to_period('M')
        sns.boxplot(x='Modification Month', y='File Size (Bytes)', data=df)
        plt.title("File Size Distribution by Modification Month")
        plt.xlabel("Modification Month")
        plt.ylabel("File Size (Bytes)")
        plt.xticks(rotation=90)
        st.pyplot(plt.gcf())
        
        # Insights and Statistics
        st.subheader("Insights and Statistics")
        creation_monthly_avg = df.groupby(df['Creation Date'].dt.to_period('M')).size().mean()
        modification_monthly_avg = df.groupby(df['Modified Date'].dt.to_period('M')).size().mean()
        
        st.write(f"Average number of files created per month: {creation_monthly_avg:.2f}")
        st.write(f"Average number of files modified per month: {modification_monthly_avg:.2f}")

        file_size_stats_by_month = df.groupby(df['Creation Date'].dt.to_period('M'))['File Size (Bytes)'].describe()
        st.write("File Size Statistics by Creation Month:")
        st.write(file_size_stats_by_month)
        
    else:
        st.error("The folder path does not exist.")
