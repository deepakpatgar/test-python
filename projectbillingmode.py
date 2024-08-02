import streamlit as st

# Title
st.title('Project Management Overview')

# Sections
st.header('1. Managed Services')
st.subheader('Key Project Challenges:')
st.write('- Service Level Expectations: Ensuring the managed services meet agreed-upon service levels.')
st.write('- Scope Creep: Additional requests from clients that impact cost and quality.')
st.write('- Integration and Compatibility: Complexities in managing and integrating systems.')

st.subheader('Success Metrics:')
st.write('- Service Uptime and Availability: e.g., 99.9% uptime.')
st.write('- Response and Resolution Times: Speed of response and resolution of issues.')
st.write('- Client Satisfaction: Feedback scores and surveys.')
st.write('- Compliance and Security: Adherence to standards like GDPR or ISO.')

# Separator
st.markdown('---')

st.header('2. Fixed Term Project')
st.subheader('Key Project Challenges:')
st.write('- Scope Changes: Delays and increased costs from changes in project scope.')
st.write('- Timeline Adherence: Staying on schedule to avoid delays.')
st.write('- Budget Overruns: Managing unforeseen issues or additional expenses.')

st.subheader('Success Metrics:')
st.write('- On-Time Delivery: Completing the project by the deadline.')
st.write('- On-Budget Delivery: Meeting the agreed budget.')
st.write('- Deliverable Quality: Meeting quality standards and specifications.')
st.write('- Client Satisfaction: Feedback regarding project outcomes.')

# Separator
st.markdown('---')

st.header('3. Time and Materials (T&M)')
st.subheader('Key Project Challenges:')
st.write('- Cost Overruns: Increased costs due to longer project duration or more resources.')
st.write('- Scope Management: Handling changes and additional requirements effectively.')
st.write('- Budget Predictability: Managing and budgeting with less predictable costs.')

st.subheader('Success Metrics:')
st.write('- Project Efficiency: Comparing hours worked to outcomes delivered.')
st.write('- Cost Control: Justifying costs against progress and deliverables.')
st.write('- Quality of Deliverables: Ensuring work meets quality standards.')
st.write('- Client Communication: Providing regular updates and clear communication.')

# Separator
st.markdown('---')

st.header('T&M Cost Control Tips')
st.write('- **Regular Tracking:** Keep a detailed record of hours worked and materials used.')
st.write('- **Detailed Invoices:** Provide clear and itemized invoices to the client.')
st.write('- **Scope Management:** Regularly review and manage changes to scope to avoid surprises.')
st.write('- **Frequent Updates:** Communicate frequently with the client about project status and potential cost changes.')

st.header('Timesheets and Expense Reports Handling')
st.subheader('Client Side:')
st.write('- **Review Timesheets:** Regularly review timesheets to ensure hours billed match project activities.')
st.write('- **Approve Expenses:** Verify and approve expenses reported by the service provider before payment.')
st.write('- **Budget Monitoring:** Monitor and compare actual costs against the project budget.')

st.subheader('Company Side:')
st.write('- **Detailed Timesheets:** Maintain accurate and detailed timesheets for all project work.')
st.write('- **Expense Reporting:** Keep detailed records of all expenses incurred during the project.')
st.write('- **Transparent Invoicing:** Provide clear and transparent invoices to the client, reflecting actual hours and expenses.')

# Footer
st.markdown('---')
st.write('For more information on managing projects effectively, please contact us.')
