import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate efforts
def calculate_efforts(no_of_resources, dev_per_day_effort, sit_per_day_effort, docs_per_day_effort, contingency, no_of_days, days_in_sprint):
    total_dev_effort = no_of_resources * dev_per_day_effort * no_of_days
    total_sit_effort = no_of_resources * sit_per_day_effort * no_of_days
    total_docs_effort = no_of_resources * docs_per_day_effort * no_of_days
    total_contingency_effort = contingency * (total_dev_effort + total_sit_effort + total_docs_effort)
    
    weekly_effort = total_dev_effort + total_sit_effort + total_docs_effort + total_contingency_effort
    sprint_effort = weekly_effort * (days_in_sprint / no_of_days)
    
    return weekly_effort, sprint_effort

# Title of the Streamlit app
st.title('Sprint Effort Estimator')

# Initialize lists to store input data
sprints = []
no_of_resources = []
dev_per_day_efforts = []
sit_per_day_efforts = []
docs_per_day_efforts = []
contingencies = []
no_of_days = []
days_in_sprints = []

# Input form for each sprint
for i in range(10):
    with st.form(f'Sprint {i+1}'):
        st.header(f'Sprint {i+1}')
        
        no_of_resources.append(st.number_input(f'Number of Resources for Sprint {i+1}', min_value=1, step=1))
        dev_per_day_efforts.append(st.number_input(f'Development Effort per Day for Sprint {i+1} (hours)', min_value=1.0, step=0.5))
        sit_per_day_efforts.append(st.number_input(f'SIT Effort per Day for Sprint {i+1} (hours)', min_value=0.0, step=0.5))
        docs_per_day_efforts.append(st.number_input(f'Documentation Effort per Day for Sprint {i+1} (hours)', min_value=0.0, step=0.5))
        contingencies.append(st.number_input(f'Contingency for Sprint {i+1} (%)', min_value=0.0, step=0.5) / 100)
        no_of_days.append(st.number_input(f'Number of Days for Sprint {i+1}', min_value=1, step=1))
        days_in_sprints.append(st.number_input(f'Number of Days in Sprint {i+1}', min_value=1, step=1))
        
        submit_button = st.form_submit_button(label='Submit')

# Calculate efforts and display the results
if st.button('Calculate Efforts'):
    weekly_efforts = []
    sprint_efforts = []

    for i in range(10):
        weekly_effort, sprint_effort = calculate_efforts(
            no_of_resources[i], dev_per_day_efforts[i], sit_per_day_efforts[i],
            docs_per_day_efforts[i], contingencies[i], no_of_days[i], days_in_sprints[i]
        )
        weekly_efforts.append(weekly_effort)
        sprint_efforts.append(sprint_effort)

    # Create a DataFrame to display the results
    df = pd.DataFrame({
        'Sprint': [f'Sprint {i+1}' for i in range(10)],
        '#NoofResources': no_of_resources,
        'DevPerDayEffort': dev_per_day_efforts,
        'SitPerDayEffort': sit_per_day_efforts,
        'DocsPerDayEffort': docs_per_day_efforts,
        'Contingency': contingencies,
        '#NoofDays': no_of_days,
        'Weekly Efforts': weekly_efforts,
        '#days in sprint': days_in_sprints,
        'Sprint Efforts (2 weeks)': sprint_efforts
    })

    st.subheader('Effort Estimation Results')
    st.dataframe(df)

    # Visualization
    st.subheader('Visualizations')
    fig, ax = plt.subplots()
    ax.plot(df['Sprint'], df['Weekly Efforts'], label='Weekly Efforts')
    ax.plot(df['Sprint'], df['Sprint Efforts (2 weeks)'], label='Sprint Efforts (2 weeks)')
    ax.set_xlabel('Sprint')
    ax.set_ylabel('Efforts (hours)')
    ax.set_title('Efforts per Sprint')
    ax.legend()
    st.pyplot(fig)

    # Download as CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='sprint_effort_estimation.csv',
        mime='text/csv',
    )
