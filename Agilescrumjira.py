import streamlit as st

# Title and description
st.title("Project Management with Agile Scrum")
st.write("""
This application provides guidelines and best practices for managing projects using Agile Scrum, with a focus on using JIRA effectively.
It includes best practices, guardrails, tips, suggestions, important tricks, and common small things that development teams often miss updating in JIRA.
""")

# Section for Best Practices
st.header("Best Practices")
best_practices = [
    "Define clear and achievable sprint goals.",
    "Maintain a prioritized and well-groomed backlog.",
    "Conduct regular sprint planning and review meetings.",
    "Ensure continuous communication and collaboration within the team.",
    "Use JIRA to create, track, and manage user stories and tasks.",
    "Regularly update JIRA tickets with the latest status and details."
]
for practice in best_practices:
    st.write(f"- {practice}")

# Section for Guardrails
st.header("Guardrails")
guardrails = [
    "Set realistic sprint durations (e.g., 2-4 weeks).",
    "Avoid scope creep by sticking to the sprint goal.",
    "Ensure all team members update their tasks in JIRA daily.",
    "Monitor the burndown chart to track progress and identify bottlenecks.",
    "Conduct regular retrospectives to identify and address improvement areas."
]
for guardrail in guardrails:
    st.write(f"- {guardrail}")

# Section for Tips
st.header("Tips")
tips = [
    "Use JIRA dashboards to get a quick overview of project status.",
    "Create custom JIRA filters to track specific aspects of the project.",
    "Leverage JIRA reports to analyze team performance and velocity.",
    "Integrate JIRA with other tools (e.g., Confluence, Slack) for better collaboration.",
    "Ensure all user stories have clear acceptance criteria."
]
for tip in tips:
    st.write(f"- {tip}")

# Section for Suggestions
st.header("Suggestions")
suggestions = [
    "Break down large user stories into smaller, manageable tasks.",
    "Use story points to estimate the effort required for each task.",
    "Regularly review and refine the backlog based on feedback and priorities.",
    "Encourage team members to log their work in JIRA daily.",
    "Use JIRA's workflow features to track the progress of tasks through different stages."
]
for suggestion in suggestions:
    st.write(f"- {suggestion}")

# Section for Important Tricks
st.header("Important Tricks")
tricks = [
    "Use JIRA's automation rules to streamline repetitive tasks.",
    "Set up notifications and reminders to keep the team informed about important updates.",
    "Create a dedicated JIRA board for tracking impediments and blockers.",
    "Use the burndown chart to identify and address sprint issues early.",
    "Leverage JIRA's API to integrate with other tools and automate workflows."
]
for trick in tricks:
    st.write(f"- {trick}")

# Section for JIRA Usage Guidelines
st.header("JIRA Usage Guidelines")
jira_guidelines = [
    "Ensure all tasks are assigned to team members with clear due dates.",
    "Regularly update the status of tasks to reflect progress accurately.",
    "Use labels and components to categorize tasks effectively.",
    "Maintain detailed descriptions and comments for each task.",
    "Use JIRA's time tracking features to log work hours accurately.",
    "Ensure the burndown chart is regularly monitored and updated."
]
for guideline in jira_guidelines:
    st.write(f"- {guideline}")

# Section for Commonly Missed Updates
st.header("Commonly Missed Updates in JIRA")
missed_updates = [
    "Updating task descriptions with new findings or changes.",
    "Logging work done after completing tasks.",
    "Transitioning tasks through the correct workflow stages.",
    "Linking related tasks and user stories.",
    "Adding necessary attachments and screenshots to tasks.",
    "Updating task estimates when scope changes.",
    "Closing tasks that are completed to keep the board clean.",
    "Documenting impediments or blockers in real-time."
]
for update in missed_updates:
    st.write(f"- {update}")

# Footer
st.write("---")
st.write("**Note:** This is a general guide for project management using Agile Scrum and JIRA. Specific strategies and practices may vary based on the project and team dynamics.")
