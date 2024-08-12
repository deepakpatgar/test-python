import streamlit as st
import pandas as pd

# Data for the project types
project_types = [
    {
        "name": "Managed Services",
        "pros": ["Predictable costs", "Continuous support and maintenance", "Focus on core business"],
        "cons": ["Long-term commitment", "Potential over-reliance on vendor"],
        "suitable_for": ["Ongoing IT support", "Maintenance projects", "Clients needing continuous service"],
        "management_style": "Kanban, Lean",
        "industry_fit": ["Finance", "Retail", "Healthcare"],
        "budget": "Medium to High",
        "resource_size": "Medium to Large",
        "tips": ["Define clear SLAs", "Regular performance reviews", "Flexibility for changing needs"],
        "bidding_tips": [
            "Understand client needs and tailor the proposal accordingly.",
            "Highlight long-term value and cost savings.",
            "Emphasize experience in similar managed services projects."
        ],
        "sow_considerations": [
            "Clearly define service levels (SLAs).",
            "Include detailed performance metrics.",
            "Specify response and resolution times for incidents."
        ],
        "rfp_tips": [
            "Respond comprehensively to each RFP requirement.",
            "Showcase relevant case studies and client testimonials.",
            "Provide a clear cost breakdown."
        ],
        "rfi_tips": [
            "Gather detailed requirements from the client.",
            "Focus on high-level capabilities and differentiators.",
            "Keep the response concise and focused."
        ]
    },
    {
        "name": "Fixed Term Project",
        "pros": ["Clear budget and timeline", "Defined scope", "Easier project management"],
        "cons": ["Less flexibility", "Scope changes can be costly", "Risk of underestimation"],
        "suitable_for": ["Projects with well-defined requirements", "Short-term engagements", "Clients with fixed budgets"],
        "management_style": "Waterfall",
        "industry_fit": ["Manufacturing", "Public Sector", "Construction"],
        "budget": "Low to Medium",
        "resource_size": "Small to Medium",
        "tips": ["Detailed initial requirements", "Change management process", "Contingency planning"]
    },
    {
        "name": "Time & Material (T&M) Project",
        "pros": ["Flexibility in scope", "Adaptability to changes", "Transparent billing"],
        "cons": ["Less cost predictability", "Requires close monitoring", "Potential for cost overruns"],
        "suitable_for": ["Agile projects", "Evolving requirements", "Long-term development"],
        "management_style": "Agile Scrum, Kanban",
        "industry_fit": ["Technology", "Startups", "Finance"],
        "budget": "Variable",
        "resource_size": "Small to Large",
        "tips": ["Regular progress tracking", "Clear communication channels", "Set budget expectations"]
    },
    {
        "name": "Milestone-Based Billing",
        "pros": ["Tied to deliverables", "Encourages timely progress", "Clear payment schedule"],
        "cons": ["Dependency on milestone definition", "Possible disputes on milestone completion"],
        "suitable_for": ["Projects with distinct phases", "Clients wanting tangible progress", "Complex projects"],
        "management_style": "Waterfall, Agile Hybrid",
        "industry_fit": ["Finance", "Technology", "Public Sector"],
        "budget": "Medium to High",
        "resource_size": "Medium to Large",
        "tips": ["Clear milestone definitions", "Regular milestone reviews", "Transparency in progress"]
    },
    {
        "name": "Performance-Based Billing",
        "pros": ["Focus on results", "Incentivizes vendor performance", "Cost-effective for clients"],
        "cons": ["High risk for vendors", "Difficult to define metrics", "Potential disputes"],
        "suitable_for": ["Outcome-focused projects", "Marketing campaigns", "Clients with clear performance metrics"],
        "management_style": "Agile Scrum, Lean",
        "industry_fit": ["Marketing", "Sales", "Finance"],
        "budget": "Variable",
        "resource_size": "Small to Medium",
        "tips": ["Define clear performance metrics", "Regular performance reviews", "Incentives for vendors"]
    },
    {
        "name": "Retainer-Based Billing",
        "pros": ["Steady revenue for vendors", "Ongoing support", "Predictable costs for clients"],
        "cons": ["Less flexibility", "Potential for underutilization", "Long-term commitment"],
        "suitable_for": ["Ongoing consultancy", "Maintenance services", "Clients needing continuous engagement"],
        "management_style": "Kanban, Lean",
        "industry_fit": ["Legal", "Consulting", "Finance"],
        "budget": "Medium to High",
        "resource_size": "Medium to Large",
        "tips": ["Define scope of retainer services", "Regular utilization reviews", "Adjust retainer terms as needed"]
    },
    {
        "name": "Cost Plus Billing",
        "pros": ["Covers all costs", "Includes profit margin", "Transparent cost structure"],
        "cons": ["Less cost control for clients", "Potential for cost overruns", "Requires detailed cost tracking"],
        "suitable_for": ["Large-scale engineering projects", "Construction projects", "Government contracts"],
        "management_style": "Waterfall",
        "industry_fit": ["Construction", "Engineering", "Public Sector"],
        "budget": "High",
        "resource_size": "Large",
        "tips": ["Detailed cost tracking", "Regular cost reviews", "Clear profit margin agreements"]
    },
    {
        "name": "Subscription-Based Billing",
        "pros": ["Regular revenue stream", "Ongoing updates and support", "Lower upfront cost for clients"],
        "cons": ["Long-term commitment", "Potential for overcharging", "Client churn risk"],
        "suitable_for": ["SaaS products", "Ongoing software access", "Clients needing continuous updates"],
        "management_style": "Kanban, Agile",
        "industry_fit": ["Technology", "Media", "Finance"],
        "budget": "Low to Medium",
        "resource_size": "Small to Medium",
        "tips": ["Regular value addition", "Client engagement strategies", "Flexible subscription terms"]
    },
    {
        "name": "Unit-Based Billing",
        "pros": ["Pay-as-you-go model", "Scalable costs", "Clear cost per unit"],
        "cons": ["Unpredictable costs", "Requires detailed tracking", "Potential for under/overutilization"],
        "suitable_for": ["Telecom services", "Cloud computing", "Clients with varying usage needs"],
        "management_style": "Lean, Agile",
        "industry_fit": ["Telecom", "Technology", "Finance"],
        "budget": "Variable",
        "resource_size": "Small to Large",
        "tips": ["Accurate usage tracking", "Clear unit definitions", "Flexible scaling options"]
    },
    {
        "name": "Capped T&M Billing",
        "pros": ["Flexibility with cost control", "Prevents cost overruns", "Balance between T&M and fixed cost"],
        "cons": ["Potential for scope limitation", "Requires close monitoring", "Negotiation on cap"],
        "suitable_for": ["Projects needing flexibility with budget constraints", "Clients with evolving needs", "Medium to long-term projects"],
        "management_style": "Agile Scrum, Waterfall",
        "industry_fit": ["Technology", "Startups", "Finance"],
        "budget": "Medium",
        "resource_size": "Small to Medium",
        "tips": ["Clear cap agreement", "Regular monitoring", "Transparency in progress and costs"]
    },
    {
        "name": "Hybrid Models",
        "pros": ["Customizable billing structure", "Balances flexibility and cost control", "Adaptable to project needs"],
        "cons": ["Complex billing management", "Potential for confusion", "Requires clear agreements"],
        "suitable_for": ["Complex projects", "Clients needing varied billing structures", "Projects with mixed requirements"],
        "management_style": "Agile Hybrid, Kanban",
        "industry_fit": ["Technology", "Healthcare", "Finance"],
        "budget": "Variable",
        "resource_size": "Small to Large",
        "tips": ["Clear billing structure definition", "Regular reviews", "Flexibility to adjust terms"]
    }
]

# Display project type details in columns
def display_project_type_details(project):
    st.header(project["name"])
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pros")
        st.write("\n".join([f"- {pro}" for pro in project["pros"]]))
        st.subheader("Cons")
        st.write("\n".join([f"- {con}" for con in project["cons"]]))
        st.subheader("Suitable For")
        st.write("\n".join([f"- {suitable}" for suitable in project["suitable_for"]]))
    
    with col2:
        st.subheader("Project Management Style")
        st.write(f"- {project['management_style']}")
        st.subheader("Industry Fit")
        st.write("\n".join([f"- {industry}" for industry in project["industry_fit"]]))
        st.subheader("Budget")
        st.write(f"- {project['budget']}")
        st.subheader("Resource Size")
        st.write(f"- {project['resource_size']}")
        st.subheader("Important Tips")
        st.write("\n".join([f"- {tip}" for tip in project["tips"]]))

st.title("Project Billing Types and Best Practices")

# Display each project type
for project_type in project_types:
    display_project_type_details(project_type)

# Function to convert project data to DataFrame
def convert_to_dataframe(project_types):
    rows = []
    for project in project_types:
        rows.append({
            "Name": project["name"],
            "Pros": "\n".join(project["pros"]),
            "Cons": "\n".join(project["cons"]),
            "Suitable For": "\n".join(project["suitable_for"]),
            "Project Management Style": project["management_style"],
            "Industry Fit": "\n".join(project["industry_fit"]),
            "Budget": project["budget"],
            "Resource Size": project["resource_size"],
            "Important Tips": "\n".join(project["tips"])
        })
    return pd.DataFrame(rows)

# Convert data to DataFrame
df = convert_to_dataframe(project_types)

# Add a download button for the CSV
st.sidebar.header("Download Data")
csv = df.to_csv(index=False)
st.sidebar.download_button(
    label="Download as CSV",
    data=csv,
    file_name="project_billing_types.csv",
    mime="text/csv"
)

# Additional Section for Vendor Tips
st.sidebar.header("Vendor Tips")
st.sidebar.write("""
- Ensure clear agreements on billing terms.
- Maintain transparency with clients.
- Regularly review project progress and billing.
- Adapt billing models based on project and client needs.
- Keep detailed records for all billable activities.
""")

