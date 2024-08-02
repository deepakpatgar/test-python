import streamlit as st

# Title and description
st.title("JIRA Setup for Data Platform Modernization Project")
st.write("""
This application provides guidelines and best practices for setting up JIRA end-to-end for a large Data Platform Modernization project. 
It covers multiple features, POD teams, Scrum meeting structure, JIRA automations, and managing many sprints and milestones.
""")

# Section for Best Practices
st.header("Best Practices")
best_practices = [
    "Define a clear project structure with components and labels.",
    "Create dedicated JIRA boards for each POD team.",
    "Use Epics to group related user stories and tasks.",
    "Set up a comprehensive workflow that covers all stages of the project.",
    "Regularly update and groom the product backlog.",
    "Leverage JIRA's reporting tools to monitor progress and performance."
]
for practice in best_practices:
    st.write(f"- {practice}")

# Section for Guardrails
st.header("Guardrails")
guardrails = [
    "Ensure consistent use of issue types and fields across the project.",
    "Maintain clear and concise user stories with well-defined acceptance criteria.",
    "Limit the number of items in the 'In Progress' column to prevent overloading the team.",
    "Set up permissions and roles to control access and modifications.",
    "Regularly review and adjust workflows and processes based on team feedback."
]
for guardrail in guardrails:
    st.write(f"- {guardrail}")

# Section for Tips
st.header("Tips")
tips = [
    "Use JIRA filters to create custom views for different stakeholders.",
    "Integrate JIRA with Confluence to document meeting notes and project details.",
    "Set up JIRA automations to streamline repetitive tasks and notifications.",
    "Utilize JIRA's roadmap feature to visualize milestones and key deliverables.",
    "Regularly review and update JIRA dashboards to reflect the latest project status."
]
for tip in tips:
    st.write(f"- {tip}")

# Section for Suggestions
st.header("Suggestions")
suggestions = [
    "Create a project charter and roadmap to outline key objectives and milestones.",
    "Define clear roles and responsibilities for each POD team.",
    "Schedule regular Scrum meetings (daily stand-ups, sprint planning, retrospectives).",
    "Use story points to estimate and track the effort required for tasks.",
    "Encourage team members to update their tasks in JIRA daily."
]
for suggestion in suggestions:
    st.write(f"- {suggestion}")

# Section for Important Tricks
st.header("Important Tricks")
tricks = [
    "Use JIRA's bulk change feature to update multiple issues at once.",
    "Set up custom workflows for different types of tasks and processes.",
    "Leverage JIRA's API to integrate with other tools and automate workflows.",
    "Use the burndown chart to monitor sprint progress and identify bottlenecks.",
    "Create JIRA filters and subscriptions to keep stakeholders informed."
]
for trick in tricks:
    st.write(f"- {trick}")

# Section for Scrum Meeting Structure
st.header("Scrum Meeting Structure")
scrum_meetings = [
    "Daily Stand-up: A short meeting to discuss what was done yesterday, what will be done today, and any blockers.",
    "Sprint Planning: A meeting to define the sprint goal and plan the tasks for the upcoming sprint.",
    "Sprint Review: A meeting to showcase completed work and gather feedback from stakeholders.",
    "Sprint Retrospective: A meeting to reflect on the sprint and identify areas for improvement."
]
for meeting in scrum_meetings:
    st.write(f"- {meeting}")

# Section for JIRA Automations
st.header("JIRA Automations")
automations = [
    "Set up rules to automatically transition tasks based on status updates.",
    "Create notifications for key events (e.g., when a task is blocked or completed).",
    "Automate the creation of sub-tasks for recurring tasks.",
    "Set up scheduled reports to monitor project progress and performance.",
    "Use webhooks to integrate JIRA with other tools and systems."
]
for automation in automations:
    st.write(f"- {automation}")

# Section for Commonly Missed Updates in JIRA
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

# Section for Confluence Setup Tips
st.header("Confluence Setup Tips")
confluence_tips = [
    "Create a space for each project or team to organize content effectively.",
    "Use templates to maintain consistency in meeting notes, project plans, and documentation.",
    "Integrate Confluence with JIRA to link project updates and issue tracking.",
    "Set up a knowledge base for frequently asked questions and troubleshooting guides.",
    "Encourage team members to document decisions and processes to create a single source of truth.",
    "Use labels and categories to organize pages and make them easily searchable.",
    "Set permissions to control access to sensitive information and maintain confidentiality.",
    "Use the Confluence calendar to schedule and track project milestones and deadlines."
]
for tip in confluence_tips:
    st.write(f"- {tip}")
    
# Footer
st.write("---")
st.write("**Note:** This guide is for setting up JIRA for a Data Platform Modernization project. Specific strategies and practices may vary based on the project's scope and team dynamics.")
