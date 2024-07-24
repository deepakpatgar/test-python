import streamlit as st

# Title
st.title("ETL and Database Cost Estimator")

# ETL Tool Costs
st.header("ETL Tool Costs")
etl_tool = st.selectbox("Select ETL Tool", ["Apache Nifi", "Talend", "Informatica", "Custom ETL"])
licensing_costs = st.number_input("Licensing Costs (USD)", value=0.0)
infrastructure_costs = st.number_input("Infrastructure Costs (USD)", value=0.0)
maintenance_costs = st.number_input("Annual Maintenance and Support Costs (%)", value=0.0)

# Database Costs
st.header("Database Costs")
database_type = st.selectbox("Select Database Type", ["Oracle", "MS SQL Server", "Snowflake", "Aurora MySQL", "AWS Redshift"])
database_licensing_costs = st.number_input("Database Licensing Costs (USD)", value=0.0)
database_infrastructure_costs = st.number_input("Database Infrastructure Costs (USD)", value=0.0)
storage_costs = st.number_input("Storage Costs (USD/month)", value=0.0)
backup_costs = st.number_input("Backup and DR Costs (USD/month)", value=0.0)

# Tables and Data Volume
st.header("Tables and Data Volume")
num_tables = st.number_input("Number of Tables", value=0)
data_volume = st.number_input("Data Volume (TB)", value=0.0)

# ETL Processes
st.header("ETL Processes")
raw_layer_processes = st.number_input("Number of Processes (Raw Layer)", value=0)
sanitize_layer_processes = st.number_input("Number of Processes (Sanitize Layer)", value=0)
conform_layer_processes = st.number_input("Number of Processes (Conform Layer)", value=0)

# Additional Costs
st.header("Additional Costs")
integration_costs = st.number_input("Data Integration Costs (USD)", value=0.0)
data_quality_costs = st.number_input("Data Quality Costs (USD)", value=0.0)
monitoring_costs = st.number_input("Monitoring and Logging Costs (USD)", value=0.0)
personnel_costs = st.number_input("Personnel Costs (USD/month)", value=0.0)

# Calculate Total Cost Estimate
total_cost_estimate = (
    licensing_costs + infrastructure_costs + maintenance_costs +
    database_licensing_costs + database_infrastructure_costs + storage_costs + backup_costs +
    integration_costs + data_quality_costs + monitoring_costs + personnel_costs
)

# Display Total Cost Estimate
st.header("Total Cost Estimate")
st.write(f"Total ROM Estimate: USD {total_cost_estimate:.2f}")

