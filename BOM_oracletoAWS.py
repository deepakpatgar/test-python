import streamlit as st

# Define constants for cost calculations (can be customized)
COST_PER_HOUR = {
    "developer": 50,
    "analyst": 60,
    "project_manager": 80,
    "tester": 40,
    "dba": 70
}
HARDWARE_COST = 2000  # Example hardware cost per unit
SOFTWARE_COST = 500  # Example software license cost per unit
CLOUD_COST = 0.1  # Example cloud cost per GB
INFRASTRUCTURE_COST = 1000  # Example infrastructure cost per unit
LICENSE_COST = 300  # Example licensing cost per unit

# AWS specific costs (these can be replaced with actual values)
AWS_REDSHIFT_COST_PER_HOUR = 0.25  # Example cost per Redshift node-hour
AWS_S3_COST_PER_GB = 0.023  # Example cost per GB of S3 storage
AWS_DATA_TRANSFER_COST_PER_GB = 0.09  # Example cost per GB for data transfer

# Function to calculate total cost
def calculate_cost(dev_hours, analyst_hours, pm_hours, tester_hours, dba_hours,
                   num_hardware, num_software, cloud_storage_gb, infrastructure_units, num_licenses,
                   redshift_hours, s3_storage_gb, data_transfer_gb):
    dev_cost = dev_hours * COST_PER_HOUR["developer"]
    analyst_cost = analyst_hours * COST_PER_HOUR["analyst"]
    pm_cost = pm_hours * COST_PER_HOUR["project_manager"]
    tester_cost = tester_hours * COST_PER_HOUR["tester"]
    dba_cost = dba_hours * COST_PER_HOUR["dba"]
    hardware_cost = num_hardware * HARDWARE_COST
    software_cost = num_software * SOFTWARE_COST
    cloud_cost = cloud_storage_gb * CLOUD_COST
    infrastructure_cost = infrastructure_units * INFRASTRUCTURE_COST
    license_cost = num_licenses * LICENSE_COST
    
    aws_redshift_cost = redshift_hours * AWS_REDSHIFT_COST_PER_HOUR
    aws_s3_cost = s3_storage_gb * AWS_S3_COST_PER_GB
    aws_data_transfer_cost = data_transfer_gb * AWS_DATA_TRANSFER_COST_PER_GB
    
    total_cost = (dev_cost + analyst_cost + pm_cost + tester_cost + dba_cost +
                  hardware_cost + software_cost + cloud_cost +
                  infrastructure_cost + license_cost +
                  aws_redshift_cost + aws_s3_cost + aws_data_transfer_cost)
    return total_cost

# Streamlit app
st.title("Bill of Materials for ETL Pipeline Build to AWS Cloud Data Warehouse")
st.header("Enter your project details:")

# Input fields for hours
dev_hours = st.number_input("Developer hours:", min_value=0, value=100)
analyst_hours = st.number_input("Analyst hours:", min_value=0, value=50)
pm_hours = st.number_input("Project Manager hours:", min_value=0, value=30)
tester_hours = st.number_input("Tester hours:", min_value=0, value=20)
dba_hours = st.number_input("DBA hours:", min_value=0, value=40)

# Input fields for quantities
num_hardware = st.number_input("Number of hardware units:", min_value=0, value=5)
num_software = st.number_input("Number of software licenses:", min_value=0, value=10)
cloud_storage_gb = st.number_input("Cloud storage (GB):", min_value=0.0, value=1000.0, step=1.0)
infrastructure_units = st.number_input("Number of infrastructure units:", min_value=0, value=3)
num_licenses = st.number_input("Number of licenses:", min_value=0, value=15)

# AWS-specific inputs
redshift_hours = st.number_input("AWS Redshift node-hours:", min_value=0.0, value=500.0, step=1.0)
s3_storage_gb = st.number_input("AWS S3 storage (GB):", min_value=0.0, value=1000.0, step=1.0)
data_transfer_gb = st.number_input("Data transfer (GB):", min_value=0.0, value=500.0, step=1.0)

# Calculate total cost
total_cost = calculate_cost(dev_hours, analyst_hours, pm_hours, tester_hours, dba_hours,
                            num_hardware, num_software, cloud_storage_gb,
                            infrastructure_units, num_licenses,
                            redshift_hours, s3_storage_gb, data_transfer_gb)

# Display total cost
st.subheader(f"Total Estimated Cost: ${total_cost:,.2f}")

# Additional customization options
st.sidebar.header("Customization Options")
COST_PER_HOUR["developer"] = st.sidebar.number_input("Developer hourly rate:", min_value=0, value=COST_PER_HOUR["developer"], step=1)
COST_PER_HOUR["analyst"] = st.sidebar.number_input("Analyst hourly rate:", min_value=0, value=COST_PER_HOUR["analyst"], step=1)
COST_PER_HOUR["project_manager"] = st.sidebar.number_input("Project Manager hourly rate:", min_value=0, value=COST_PER_HOUR["project_manager"], step=1)
COST_PER_HOUR["tester"] = st.sidebar.number_input("Tester hourly rate:", min_value=0, value=COST_PER_HOUR["tester"], step=1)
COST_PER_HOUR["dba"] = st.sidebar.number_input("DBA hourly rate:", min_value=0, value=COST_PER_HOUR["dba"], step=1)
HARDWARE_COST = st.sidebar.number_input("Hardware cost per unit:", min_value=0, value=HARDWARE_COST, step=100)
SOFTWARE_COST = st.sidebar.number_input("Software cost per unit:", min_value=0, value=SOFTWARE_COST, step=100)
CLOUD_COST = st.sidebar.number_input("Cloud cost per GB:", min_value=0.0, value=CLOUD_COST, step=0.01)
INFRASTRUCTURE_COST = st.sidebar.number_input("Infrastructure cost per unit:", min_value=0, value=INFRASTRUCTURE_COST, step=100)
LICENSE_COST = st.sidebar.number_input("License cost per unit:", min_value=0, value=LICENSE_COST, step=10)
AWS_REDSHIFT_COST_PER_HOUR = st.sidebar.number_input("AWS Redshift cost per hour:", min_value=0.0, value=AWS_REDSHIFT_COST_PER_HOUR, step=0.01)
AWS_S3_COST_PER_GB = st.sidebar.number_input("AWS S3 cost per GB:", min_value=0.0, value=AWS_S3_COST_PER_GB, step=0.01)
AWS_DATA_TRANSFER_COST_PER_GB = st.sidebar.number_input("AWS Data transfer cost per GB:", min_value=0.0, value=AWS_DATA_TRANSFER_COST_PER_GB, step=0.01)

# Recalculate cost with customization options
total_cost_custom = calculate_cost(dev_hours, analyst_hours, pm_hours, tester_hours, dba_hours,
                                   num_hardware, num_software, cloud_storage_gb,
                                   infrastructure_units, num_licenses,
                                   redshift_hours, s3_storage_gb, data_transfer_gb)

# Display customized total cost
st.sidebar.subheader(f"Customized Total Estimated Cost: ${total_cost_custom:,.2f}")
