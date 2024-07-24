import streamlit as st
import pandas as pd
import os

# Title
st.title("Personal Finance Dashboard")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Income and Expenses", "Investments", "Financial Metrics"])

# Function to check if a CSV file exists and is not empty
def csv_file_exists_and_not_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) > 0

# Load existing data from CSV files or create new DataFrames
income_file_path = 'income.csv'
if csv_file_exists_and_not_empty(income_file_path):
    income_data = pd.read_csv(income_file_path)
else:
    income_data = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

expenses_file_path = 'expenses.csv'
if csv_file_exists_and_not_empty(expenses_file_path):
    expenses_data = pd.read_csv(expenses_file_path)
else:
    expenses_data = pd.DataFrame(columns=['Date', 'Description', 'Amount'])

investment_file_path = 'investments.csv'
if csv_file_exists_and_not_empty(investment_file_path):
    investment_data = pd.read_csv(investment_file_path)
else:
    investment_data = pd.DataFrame(columns=['Date', 'Description', 'Invested Amount (INR)', 'Current Value (INR)'])

# Input forms for income and expenses
if menu == "Income and Expenses":
    st.header("Income and Expenses")

    # Input form for income
    st.subheader("Add Income")
    income_date = st.date_input("Date (Income)", pd.to_datetime('today'), key='income_date')
    income_description = st.text_input("Description (Income)")
    income_amount = st.number_input("Amount (INR) (Income)", step=1.0)
    if st.button("Add Income"):
        new_income = {'Date': income_date, 'Description': income_description, 'Amount': income_amount}
        income_data = pd.concat([income_data, pd.DataFrame([new_income])], ignore_index=True)

    # Input form for expenses
    st.subheader("Add Expenses")
    expenses_date = st.date_input("Date (Expenses)", pd.to_datetime('today'), key='expenses_date')
    expenses_description = st.text_input("Description (Expenses)")
    expenses_amount = st.number_input("Amount (INR) (Expenses)", step=1.0)
    if st.button("Add Expenses"):
        new_expenses = {'Date': expenses_date, 'Description': expenses_description, 'Amount': -expenses_amount}
        expenses_data = pd.concat([expenses_data, pd.DataFrame([new_expenses])], ignore_index=True)

    # Display income and expenses tables
    st.subheader("Income")
    st.dataframe(income_data)

    st.subheader("Expenses")
    st.dataframe(expenses_data)

# Input form for investments
elif menu == "Investments":
    st.header("Investments")

    st.subheader("Add Investments")
    investment_date = st.date_input("Date (Investments)", pd.to_datetime('today'), key='investment_date')
    investment_description = st.text_input("Description (Investments)")
    invested_amount = st.number_input("Invested Amount (INR)", step=1.0)
    current_value = st.number_input("Current Value (INR)", step=1.0)
    if st.button("Add Investment"):
        new_investment = {'Date': investment_date, 'Description': investment_description, 'Invested Amount (INR)': invested_amount, 'Current Value (INR)': current_value}
        investment_data = pd.concat([investment_data, pd.DataFrame([new_investment])], ignore_index=True)

    st.dataframe(investment_data)

# Display financial metrics
elif menu == "Financial Metrics":
    st.header("Financial Metrics")
    
    # Calculate and display financial metrics
    total_income = income_data['Amount'].sum()
    total_expenses = expenses_data['Amount'].sum()
    net_income = total_income + total_expenses

    st.subheader("Income Statement")
    st.write("Income: INR {:.2f}".format(total_income))
    st.write("Expenses: INR {:.2f}".format(total_expenses))
    st.write("Net Income: INR {:.2f}".format(net_income))

    # Calculate and display investment metrics
    total_invested_amount = investment_data['Invested Amount (INR)'].sum()
    total_current_value = investment_data['Current Value (INR)'].sum()
    investment_returns = total_current_value - total_invested_amount

    st.subheader("Investment Performance")
    st.write("Total Invested Amount: INR {:.2f}".format(total_invested_amount))
    st.write("Total Current Value: INR {:.2f}".format(total_current_value))
    st.write("Investment Returns: INR {:.2f}".format(investment_returns))

# Save data to CSV files
income_data.to_csv(income_file_path, index=False)
expenses_data.to_csv(expenses_file_path, index=False)
investment_data.to_csv(investment_file_path, index=False)




