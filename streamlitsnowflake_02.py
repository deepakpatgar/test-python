import streamlit as st
import snowflake.connector

# Title
st.title("Snowflake User and Access Management")

# Sidebar for Snowflake connection details
st.sidebar.header("Snowflake Connection")
account = st.sidebar.text_input("Account URL")
username = st.sidebar.text_input("Admin Username")
password = st.sidebar.text_input("Admin Password", type="password")

# Function to establish Snowflake connection
def create_snowflake_connection():
    try:
        conn = snowflakeguidelines.connector.connect(
            user=username,
            password=password,
            account=account,
        )
        return conn
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")
        return None

# Function to list users
def list_users(connection):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW USERS")
            users = cursor.fetchall()
            cursor.close()
            return users
        except Exception as e:
            st.error(f"Error listing users: {str(e)}")
            return None

# Main content
st.header("User Management")

# List users
st.subheader("List of Users")
connection = create_snowflake_connection()
if connection:
    users = list_users(connection)
    if users:
        for user in users:
            st.write(user[0])

# Add or remove user access (not implemented in this example)
st.header("Add/Remove User Access")

# You can add user access management components here

# Connection status
st.sidebar.subheader("Connection Status")
if create_snowflake_connection():
    st.sidebar.success("Connected")
else:
    st.sidebar.error("Not Connected")

