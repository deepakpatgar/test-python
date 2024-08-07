import streamlit as st

# Title of the Streamlit app
st.title('Effort Estimator')

# Input fields for various parameters
num_resources = st.number_input('Number of Resources', min_value=1, step=1)
per_day_effort = st.number_input('Effort per Resource per Day (hours)', min_value=1.0, step=0.5)
total_days_for_dev = st.number_input('Total Development Days Needed', min_value=1.0, step=0.5)
contingency_percentage = st.number_input('Contingency Percentage (%)', min_value=0.0, step=0.5)

# Calculate development effort
dev_effort = num_resources * per_day_effort * total_days_for_dev

# Calculate derived efforts
ut_effort = 0.1 * dev_effort
code_review_effort = 0.05 * ut_effort
documentation_effort = 0.05 * dev_effort

# Calculate total efforts
total_effort_without_contingency = dev_effort + ut_effort + code_review_effort + documentation_effort
contingency_effort = (contingency_percentage / 100) * total_effort_without_contingency
total_effort_with_contingency = total_effort_without_contingency + contingency_effort

# Calculate total days needed considering 8 hours per day
total_days_needed = total_effort_with_contingency / (num_resources * 8)

# Display the results
st.subheader('Effort Breakdown')
st.write(f'Development Effort: {dev_effort} hours')
st.write(f'Unit Testing Effort (10% of Dev): {ut_effort} hours')
st.write(f'Code Review Effort (5% of UT): {code_review_effort} hours')
st.write(f'Documentation Effort (5% of Dev): {documentation_effort} hours')
st.write(f'Contingency Effort: {contingency_effort} hours')

st.subheader('Total Effort')
st.write(f'Total Effort without Contingency: {total_effort_without_contingency} hours')
st.write(f'Total Effort with Contingency: {total_effort_with_contingency} hours')

st.subheader('Total Days Needed')
st.write(f'Total Days Needed: {total_days_needed:.2f} days')
