import streamlit as st
import snowflake.connector
import pandas as pd

# Title
st.title("Snowflake Data Loading and Integration")

# Sidebar for Snowflake connection details
st.sidebar.header("Snowflake Connection")
account = st.sidebar.text_input("Account URL")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
database = st.sidebar.text_input("Database")
warehouse = st.sidebar.text_input("Warehouse")
schema = st.sidebar.text_input("Schema")
table_name = st.sidebar.text_input("Target Table Name")

# Function to establish Snowflake connection
def create_snowflake_connection():
    try:
        conn = snowflakeguidelines.connector.connect(
            user=username,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        return conn
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")
        return None

# Function to perform batch data loading
def load_data_to_snowflake(connection, df, table_name):
    if connection:
        try:
            cursor = connection.cursor()
            
            # Create or replace the target table
            create_table_sql = f"CREATE OR REPLACE TABLE {table_name} ({', '.join(df.columns)})"
            cursor.execute(create_table_sql)
            
            # Copy data to Snowflake
            cursor.copy_into(table_name, df)
            cursor.close()
            
            st.success("Data loaded successfully to Snowflake.")
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")

# Main content
st.header("Batch Data Loading to Snowflake")

# Upload a CSV file for batch loading
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the DataFrame
        st.subheader("Uploaded Data Preview")
        st.dataframe(df)
        
        # Load data to Snowflake
        if st.button("Load Data to Snowflake"):
            connection = create_snowflake_connection()
            if connection:
                load_data_to_snowflake(connection, df, table_name)
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Monitoring and reporting (not implemented in this example)
st.header("Data Loading Process Monitoring")

# You can add monitoring and reporting components here

# Connection status
st.sidebar.subheader("Connection Status")
if create_snowflake_connection():
    st.sidebar.success("Connected")
else:
    st.sidebar.error("Not Connected")




