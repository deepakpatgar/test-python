import streamlit as st
from datetime import date
from fpdf import FPDF

# Title
st.title("Statement of Work (SOW) Preparation")

# Project Type Selection
project_type = st.selectbox(
    "Select Project Type",
    ("Data Migration to Cloud from Legacy Systems", 
     "Data Platform Modernization to Cloud", 
     "ETL Project")
)

# Common Inputs
st.header("Project Details")
client_name = st.text_input("Client Name")
project_name = st.text_input("Project Name")
project_start_date = st.date_input("Project Start Date", date.today())
project_end_date = st.date_input("Project End Date")
project_description = st.text_area("Project Description")

# Custom Inputs for each Project Type
if project_type == "Data Migration to Cloud from Legacy Systems":
    st.header("Legacy Systems Migration Details")
    legacy_systems = st.text_area("Legacy Systems Details")
    data_volume = st.text_input("Data Volume (in TB)")
    cloud_provider = st.text_input("Target Cloud Provider")

elif project_type == "Data Platform Modernization to Cloud":
    st.header("Data Platform Modernization Details")
    current_platform = st.text_area("Current Platform Details")
    modernization_goals = st.text_area("Modernization Goals")
    target_cloud_platform = st.text_input("Target Cloud Platform")

elif project_type == "ETL Project":
    st.header("ETL Project Details")
    source_systems = st.text_area("Source Systems Details")
    target_system = st.text_input("Target System")
    etl_tools = st.text_input("ETL Tools")
    data_transformation_requirements = st.text_area("Data Transformation Requirements")

# Generate SOW
if st.button("Generate SOW"):
    st.header("Statement of Work (SOW)")

    # Common SOW Content
    sow_content = f"""
    **Client Name:** {client_name}
    **Project Name:** {project_name}
    **Project Start Date:** {project_start_date}
    **Project End Date:** {project_end_date}
    **Project Type:** {project_type}
    **Project Description:** {project_description}
    """

    if project_type == "Data Migration to Cloud from Legacy Systems":
        sow_content += f"""
        **Legacy Systems Details:** {legacy_systems}
        **Data Volume:** {data_volume} TB
        **Target Cloud Provider:** {cloud_provider}
        """

    elif project_type == "Data Platform Modernization to Cloud":
        sow_content += f"""
        **Current Platform Details:** {current_platform}
        **Modernization Goals:** {modernization_goals}
        **Target Cloud Platform:** {target_cloud_platform}
        """

    elif project_type == "ETL Project":
        sow_content += f"""
        **Source Systems Details:** {source_systems}
        **Target System:** {target_system}
        **ETL Tools:** {etl_tools}
        **Data Transformation Requirements:** {data_transformation_requirements}
        """

    sow_content += """
    **Deliverables:**
    - Project Plan
    - Design Documents
    - Implementation and Migration
    - Testing and Validation
    - Documentation
    - Training and Support

    **Assumptions and Dependencies:**
    - Access to legacy systems and cloud environments
    - Timely provision of required resources
    - Client's availability for meetings and feedback

    **Project Milestones and Timeline:**
    - Initial Assessment and Planning: 2 weeks
    - Design Phase: 4 weeks
    - Implementation Phase: 8 weeks
    - Testing and Validation: 2 weeks
    - Final Deployment and Support: 2 weeks

    **Project Management:**
    The project will be managed using Agile methodologies with regular updates and reviews.

    **Pricing and Payment Terms:**
    The total cost of the project is $XXX,XXX. Payment will be made in milestones, as agreed upon with the client.

    **Signatures:**
    ______________________  ______________________
    Client Signature           Project Manager Signature

    Date: ____________________
    """
    
    st.write(sow_content)

    # Function to generate PDF
    def generate_pdf(content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        
        for line in content.split('\n'):
            pdf.multi_cell(0, 10, line)
        
        return pdf.output(dest='S').encode('latin1')

    # Download PDF
    pdf_bytes = generate_pdf(sow_content)
    st.download_button(
        label="Download SOW as PDF",
        data=pdf_bytes,
        file_name=f"SOW_{project_name}.pdf",
        mime="application/pdf"
    )
