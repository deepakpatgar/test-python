import streamlit as st
import pandas as pd

# Title
st.title("Automated Testing and Quality Assurance Dashboard")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Test Results", "Report Issues"])

# Sample data for test results
test_results = pd.DataFrame({
    "Test Case": ["Data Ingestion", "Data Transformation", "Data Validation", "Data Loading", "Data Export"],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],
    "Timestamp": ["2023-09-01 10:30:00", "2023-09-02 11:45:00", "2023-09-03 14:15:00", "2023-09-04 16:00:00", "2023-09-05 09:30:00"]
})

# Sample data for reported issues
reported_issues = pd.DataFrame({
    "Issue ID": ["ETL-001", "ETL-002", "ETL-003", "ETL-004"],
    "Description": ["Data Validation Failure", "Data Loading Error", "Data Ingestion Timeout", "Data Export Format Issue"],
    "Status": ["Open", "In Progress", "Closed", "Open"]
})

# Test Results
if menu == "Test Results":
    st.header("Test Results")

    # Display test results table
    st.subheader("Test Execution Status")
    st.dataframe(test_results)

# Report Issues
elif menu == "Report Issues":
    st.header("Report Issues")

    # Input form for reporting issues
    st.subheader("Report a New Issue")
    issue_description = st.text_area("Issue Description")
    issue_status = st.selectbox("Issue Status", ["Open", "In Progress", "Closed"])
    if st.button("Report Issue"):
        # Simulate reporting the issue (in a real application, this would go to a database or issue tracking system)
        new_issue = {"Issue ID": f"ETL-{len(reported_issues) + 1}", "Description": issue_description, "Status": issue_status}
        reported_issues = reported_issues.append(new_issue, ignore_index=True)
        st.success("Issue reported successfully!")

    # Display reported issues table
    st.subheader("Reported Issues")
    st.dataframe(reported_issues)

# Integration with CI Pipeline
st.sidebar.header("Continuous Integration (CI) Integration")
ci_pipeline_url = st.sidebar.text_input("Enter CI Pipeline URL")
if st.sidebar.button("Run CI Pipeline"):
    # Simulate triggering the CI pipeline (in a real application, this would invoke the CI system)
    st.success(f"CI Pipeline triggered. URL: {ci_pipeline_url}")

# About
st.sidebar.info("This is a Streamlit app for ETL testing and QA. Data is for demonstration purposes only.")
