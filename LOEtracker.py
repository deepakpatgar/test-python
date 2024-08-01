import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="ETL Project Management", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Migration Plan", "LOE Estimation Driver", "LOE Tracker", "Scope and LOE Analysis"])

# Function to show migration plan
def show_migration_plan():
    st.title("Migration Plan")
    st.markdown("### ETL Project Migration Plan")
    st.write("""
    - **Source Systems**: Databases, files
    - **Target Systems**: Cloud databases
    - **ETL Tools**: [Add your ETL tools here]
    - **Scheduling Tools**: [Add your scheduling tools here]
    - **Data Governance**: [Add your data governance practices here]
    - **Data Cleaning**: [Describe your data cleaning processes here]
    - **Staging**: [Describe your staging processes here]
    - **Layered Data Platform**: [Describe your layered data platform here]
    - **Dashboards and Reports**: [Describe your dashboards and reports here]
    """)
    
    # Example of adding more details
    source_systems = st.text_input("Source Systems", "Databases, files")
    target_systems = st.text_input("Target Systems", "Cloud databases")
    etl_tools = st.text_input("ETL Tools", "ETL Tool 1, ETL Tool 2")
    scheduling_tools = st.text_input("Scheduling Tools", "Scheduling Tool 1, Scheduling Tool 2")
    data_governance = st.text_area("Data Governance", "Describe your data governance practices here")
    data_cleaning = st.text_area("Data Cleaning", "Describe your data cleaning processes here")
    staging = st.text_area("Staging", "Describe your staging processes here")
    layered_data_platform = st.text_area("Layered Data Platform", "Describe your layered data platform here")
    dashboards_reports = st.text_area("Dashboards and Reports", "Describe your dashboards and reports here")
    
# Function to show LOE estimation driver
def show_loe_estimation_driver():
    st.title("LOE Estimation Driver")
    st.markdown("### Level of Effort Estimation")
    
    # Example input fields for estimation
    source_complexity = st.slider("Source Complexity", 1, 5)
    target_complexity = st.slider("Target Complexity", 1, 5)
    data_volume = st.number_input("Data Volume (GB)", min_value=0)
    transformation_complexity = st.slider("Transformation Complexity", 1, 5)
    testing_effort = st.slider("Testing Effort", 1, 5)
    
    # Simple estimation calculation
    estimated_loe = (source_complexity + target_complexity + transformation_complexity + testing_effort) * data_volume / 100
    st.write(f"Estimated LOE: {estimated_loe} person-hours")
    
# Function to show LOE tracker
def show_loe_tracker():
    st.title("LOE Tracker")
    st.markdown("### Track Level of Effort for Each Task")
    
    # Example DataFrame for LOE tracking
    loe_data = pd.DataFrame({
        "Task": ["Extract Data", "Transform Data", "Load Data", "Testing"],
        "Assigned To": ["Person A", "Person B", "Person C", "Person D"],
        "Estimated LOE (hrs)": [10, 15, 20, 5],
        "Actual LOE (hrs)": [8, 18, 22, 6]
    })
    
    st.table(loe_data)
    
# Function to show scope and LOE analysis
def show_scope_loe_analysis():
    st.title("Scope and LOE Analysis")
    st.markdown("### Analyze the Scope and Level of Effort for ETL Projects")
    
    # Example input fields for scope and LOE analysis
    scope = st.text_area("Scope Description", "Describe the scope of your ETL project here")
    source_systems_count = st.number_input("Number of Source Systems", min_value=1)
    target_systems_count = st.number_input("Number of Target Systems", min_value=1)
    etl_tools_used = st.multiselect("ETL Tools Used", ["ETL Tool 1", "ETL Tool 2", "ETL Tool 3"])
    
    # Simple scope analysis output
    st.write(f"Total Source Systems: {source_systems_count}")
    st.write(f"Total Target Systems: {target_systems_count}")
    st.write(f"ETL Tools Used: {', '.join(etl_tools_used)}")
    
    # Example chart for LOE analysis
    loe_analysis_data = pd.DataFrame({
        "Phase": ["Extraction", "Transformation", "Loading", "Testing"],
        "LOE": [source_systems_count * 10, source_systems_count * 20, target_systems_count * 15, source_systems_count * 5]
    })
    st.bar_chart(loe_analysis_data.set_index("Phase"))
    
# Show selected page based on navigation
if options == "Migration Plan":
    show_migration_plan()
elif options == "LOE Estimation Driver":
    show_loe_estimation_driver()
elif options == "LOE Tracker":
    show_loe_tracker()
elif options == "Scope and LOE Analysis":
    show_scope_loe_analysis()
