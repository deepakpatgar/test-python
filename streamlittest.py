import streamlit as st

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.selectbox("Select an operation:", ["Addition", "Subtraction"])

    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2

    st.write(f"Result of {operation}: {result}")

if __name__ == "__main__":
    main()
