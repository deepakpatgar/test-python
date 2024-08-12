import streamlit as st

# Sidebar for selecting the project management tool and methodology
st.sidebar.title("Project Management Guide")
tool = st.sidebar.selectbox("Select Tool", ["Jira", "Asana", "Others"])
methodology = st.sidebar.selectbox("Select Methodology", ["Scrum", "Kanban", "Waterfall", "Other"])

# Function to display content based on tool and methodology
def display_guide(tool, methodology):
    if tool == "Jira":
        st.header(f"Jira - {methodology} Guide")
        if methodology == "Scrum":
            display_jira_scrum()
        elif methodology == "Kanban":
            display_jira_kanban()
        elif methodology == "Waterfall":
            display_jira_waterfall()
        else:
            st.write("No specific guide available.")
    elif tool == "Asana":
        st.header(f"Asana - {methodology} Guide")
        if methodology == "Scrum":
            display_asana_scrum()
        elif methodology == "Kanban":
            display_asana_kanban()
        elif methodology == "Waterfall":
            display_asana_waterfall()
        else:
            st.write("No specific guide available.")
    else:
        st.header(f"{tool} - {methodology} Guide")
        st.write("Content coming soon.")

# Jira Scrum Guide
def display_jira_scrum():
    st.subheader("Best Practices")
    st.write("""
    1. Create clear and concise user stories with acceptance criteria.
    2. Use story points for estimation to gauge effort.
    3. Maintain a consistent sprint duration (usually 2-4 weeks).
    4. Regularly conduct backlog grooming sessions.
    5. Prioritize tasks based on business value and urgency.
    6. Use Jira Automation to streamline repetitive tasks.
    7. Encourage team collaboration via comments and mentions.
    8. Track sprint progress with burndown charts.
    9. Perform sprint retrospectives to improve future sprints.
    10. Integrate Jira with CI/CD tools for seamless development.
    """)
    st.subheader("Standards")
    st.write("""
    1. Consistent naming conventions for Epics, User Stories, and Tasks.
    2. Standard labels for categorization (e.g., "bug", "feature", "improvement").
    3. Define workflows that align with Scrum ceremonies.
    4. Use standardized story point ranges (e.g., Fibonacci sequence).
    5. Implement standard fields like "Story Points", "Priority", and "Due Date".
    6. Define clear roles and responsibilities within Jira.
    7. Use consistent sprint naming conventions.
    8. Establish standard Jira dashboard views.
    9. Implement a standard template for creating user stories.
    10. Consistent use of status categories (To Do, In Progress, Done).
    """)
    st.subheader("Nomenclature")
    st.write("""
    1. **Epic**: A large body of work that can be broken down into stories.
    2. **User Story**: A piece of functionality described from the user's perspective.
    3. **Task**: Specific work required to complete a story.
    4. **Sprint**: A time-boxed period to complete a set of work.
    5. **Backlog**: A prioritized list of work for the team.
    6. **Burndown Chart**: A graphical representation of work left to do vs. time.
    7. **Acceptance Criteria**: Conditions that must be met for a story to be complete.
    8. **Velocity**: The amount of work a team can complete in a sprint.
    9. **Definition of Done (DoD)**: A shared understanding of what it means for work to be complete.
    10. **Scrum Master**: The facilitator of the Scrum process.
    """)
    st.subheader("Guardrails")
    st.write("""
    1. Avoid overcommitting in sprints to prevent burnout.
    2. Ensure all work is tracked within Jira to maintain visibility.
    3. Regularly review and refine the backlog to keep it relevant.
    4. Limit work in progress (WIP) to avoid bottlenecks.
    5. Ensure clear communication within the team about task status.
    6. Protect the sprint from scope creep by adhering to DoD.
    7. Regularly update Jira to reflect the current status of tasks.
    8. Avoid closing sprints with incomplete tasks; carry them over properly.
    9. Use Jira permissions to control access and avoid unauthorized changes.
    10. Regularly review Jira workflows to ensure they align with team practices.
    """)
    st.subheader("Important Tips")
    st.write("""
    1. Use Jira’s filtering and querying capabilities to create custom views.
    2. Leverage Jira’s integration with Confluence for documentation.
    3. Customize Jira dashboards for different team roles.
    4. Regularly archive completed sprints to keep the board clean.
    5. Utilize Jira’s bulk edit feature for managing multiple issues.
    6. Encourage the team to add detailed comments on tasks.
    7. Automate repetitive tasks using Jira’s built-in automation rules.
    8. Use labels consistently for easier filtering and reporting.
    9. Regularly review sprint velocity and adjust sprint planning accordingly.
    10. Keep an eye on the Jira Roadmap to manage long-term planning.
    """)

# Jira Kanban Guide
def display_jira_kanban():
    st.subheader("Best Practices")
    st.write("""
    1. Limit Work In Progress (WIP) to prevent bottlenecks.
    2. Prioritize tasks based on urgency and importance.
    3. Regularly review and refine the backlog.
    4. Use swimlanes to categorize tasks by priority or team.
    5. Implement a pull system where work is "pulled" into the next stage.
    6. Use Jira’s card colors to differentiate task types.
    7. Regularly update task status to reflect current progress.
    8. Track cumulative flow to identify bottlenecks.
    9. Use Kanban boards for continuous delivery without fixed sprints.
    10. Regularly review WIP limits to optimize flow.
    """)
    st.subheader("Standards")
    st.write("""
    1. Consistent naming conventions for Kanban boards and tasks.
    2. Use of color-coded labels for task status and priority.
    3. Standard columns such as Backlog, To Do, In Progress, Done.
    4. Define standard WIP limits for each stage.
    5. Use consistent task descriptions and acceptance criteria.
    6. Implement a standardized review process before moving tasks to Done.
    7. Use Jira’s built-in templates for common Kanban board setups.
    8. Define standard rules for moving tasks between columns.
    9. Implement consistent tagging for easy filtering and reporting.
    10. Establish standard board views for different roles (e.g., developer, manager).
    """)
    st.subheader("Nomenclature")
    st.write("""
    1. **Backlog**: The list of tasks to be completed.
    2. **WIP (Work In Progress)**: Tasks that are currently being worked on.
    3. **Swimlane**: A horizontal section on the Kanban board to group tasks.
    4. **Pull System**: A workflow where tasks are pulled to the next stage when capacity is available.
    5. **Cumulative Flow Diagram**: A chart showing the number of tasks in each stage over time.
    6. **Blocked**: A task that cannot proceed due to an issue.
    7. **Cycle Time**: The time it takes for a task to go from start to finish.
    8. **Lead Time**: The time from when a task is added to the backlog until it's completed.
    9. **Throughput**: The number of tasks completed in a given time period.
    10. **Kanban**: A method for visualizing work, managing flow, and limiting WIP.
    """)
    st.subheader("Guardrails")
    st.write("""
    1. Regularly update task status to reflect current progress.
    2. Keep WIP limits in place to prevent overload.
    3. Ensure tasks in the Done column meet the definition of done.
    4. Avoid multitasking to maintain focus on current WIP.
    5. Regularly review the backlog to ensure prioritization aligns with business goals.
    6. Monitor cumulative flow to identify and resolve bottlenecks.
    7. Use board filters to focus on specific tasks or categories.
    8. Ensure tasks are broken down into manageable chunks.
    9. Avoid overcomplicating the board with too many columns or swimlanes.
    10. Review and adjust WIP limits based on team capacity and performance.
    """)
    st.subheader("Important Tips")
    st.write("""
    1. Use Jira’s Quick Filters to easily switch between different views.
    2. Customize card layout to display key information upfront.
    3. Use the Jira Kanban backlog to manage tasks that are not yet ready for the board.
    4. Integrate Jira with Slack for real-time task updates.
    5. Regularly review the Done column and archive completed tasks.
    6. Use Jira’s Automation to automate task transitions based on status updates.
    7. Regularly monitor and adjust WIP limits to optimize workflow.
    8. Leverage Jira’s reporting tools to gain insights into team performance.
    9. Use Jira’s REST API for advanced reporting and integrations.
    10. Keep the board clean and organized for easy navigation and task tracking.
    """)

# Jira Waterfall Guide
def display_jira_waterfall():
    st.subheader("Best Practices")
    st.write("""
    1. Clearly define project phases and milestones.
    2. Use Gantt charts to track progress against timelines.
    3. Ensure all project requirements are clearly documented before starting.
    4. Regularly update the project plan based on actual progress.
    5. Conduct phase-end reviews to assess progress and make adjustments.
    6. Implement strict change control processes to manage scope.
    7. Use Jira’s dependency tracking to manage task dependencies.
    8. Regularly communicate with stakeholders to provide project updates.
    9. Monitor project risks and implement mitigation strategies.
    10. Ensure that all deliverables are completed and signed off at the end of each phase.
    """)
    st.subheader("Standards")
    st.write("""
    1. Naming conventions for project phases and tasks.
    2. Standard templates for project plans and documentation.
    3. Use of Gantt charts for planning and tracking.
    4. Consistent status reporting at regular intervals.
    5. Define roles and responsibilities clearly within Jira.
    6. Standardize task descriptions and acceptance criteria.
    7. Use Jira’s issue types to categorize tasks by phase.
    8. Implement standardized workflows for task approval and sign-off.
    9. Use consistent risk management and mitigation processes.
    10. Ensure all project documentation is stored in a central location.
    """)
    st.subheader("Nomenclature")
    st.write("""
    1. **Phase**: A stage in the project lifecycle.
    2. **Milestone**: A significant event in the project timeline.
    3. **Gantt Chart**: A visual representation of the project schedule.
    4. **Task Dependency**: A relationship between tasks where one depends on the completion of another.
    5. **Critical Path**: The sequence of tasks that determines the project duration.
    6. **Change Request**: A formal request to alter the project scope.
    7. **Baseline**: The original project plan, used as a reference.
    8. **Risk Management**: The process of identifying, assessing, and mitigating risks.
    9. **Stakeholder**: An individual or group with an interest in the project’s outcome.
    10. **Deliverable**: A tangible or intangible output of a project phase.
    """)
    st.subheader("Guardrails")
    st.write("""
    1. Avoid scope creep by adhering to the original project plan.
    2. Ensure all task dependencies are clearly defined and managed.
    3. Monitor the project timeline closely to avoid delays.
    4. Implement a strict change control process to manage any changes.
    5. Regularly review project risks and update mitigation strategies.
    6. Ensure that each project phase is completed before moving to the next.
    7. Communicate regularly with stakeholders to keep them informed.
    8. Use Jira’s reporting tools to track progress against the project plan.
    9. Ensure all deliverables meet the defined acceptance criteria.
    10. Conduct a post-project review to identify lessons learned.
    """)
    st.subheader("Important Tips")
    st.write("""
    1. Use Jira’s timeline view to get an overview of the project schedule.
    2. Break down large tasks into smaller, manageable sub-tasks.
    3. Regularly review the project plan and make adjustments as needed.
    4. Use Jira’s reporting tools to generate progress reports for stakeholders.
    5. Implement a robust risk management process to identify and mitigate risks.
    6. Use Jira’s dependency tracking to manage task dependencies effectively.
    7. Regularly communicate with the project team to ensure everyone is aligned.
    8. Use Jira’s integrations with Confluence for project documentation.
    9. Keep stakeholders informed of any changes to the project scope or timeline.
    10. Use Jira’s custom fields to capture additional project-specific information.
    """)

# Asana Scrum Guide (similar to Jira Scrum)
def display_asana_scrum():
    st.subheader("Best Practices")
    st.write("""
    1. Utilize Asana’s custom fields for tracking story points.
    2. Create templates for recurring tasks to save time.
    3. Use Asana’s timeline view to plan sprints visually.
    4. Regularly conduct sprint retrospectives to improve processes.
    5. Leverage Asana’s project templates to standardize workflows.
    6. Utilize Asana’s task dependencies to manage workload.
    7. Encourage team collaboration via task comments and mentions.
    8. Use sections within projects to represent different sprint stages.
    9. Regularly review and refine the product backlog.
    10. Use Asana’s reporting features to track sprint progress.
    """)
    # Add more sections similarly to the Jira Scrum guide

# Asana Kanban Guide (similar to Jira Kanban)
def display_asana_kanban():
    st.subheader("Best Practices")
    st.write("""
    1. Use Asana’s board view to manage tasks visually.
    2. Limit WIP to avoid overload and maintain focus.
    3. Utilize color-coded tags to differentiate task types.
    4. Regularly review the board to reprioritize tasks.
    5. Use Asana’s task dependencies to manage workload.
    6. Implement a pull system for task transitions.
    7. Track task progress using Asana’s timeline view.
    8. Encourage team collaboration via task comments and mentions.
    9. Regularly update task status to reflect current progress.
    10. Use Asana’s reporting features to gain insights into workflow efficiency.
    """)
    # Add more sections similarly to the Jira Kanban guide

# Asana Waterfall Guide (similar to Jira Waterfall)
def display_asana_waterfall():
    st.subheader("Best Practices")
    st.write("""
    1. Utilize Asana’s timeline view to manage project phases.
    2. Use task dependencies to track progress across project stages.
    3. Clearly define project phases and milestones.
    4. Implement strict change control processes.
    5. Regularly update the project plan based on actual progress.
    6. Conduct phase-end reviews to assess project status.
    7. Use Asana’s custom fields to track important project metrics.
    8. Communicate regularly with stakeholders.
    9. Monitor project risks and implement mitigation strategies.
    10. Ensure all deliverables are completed and signed off at the end of each phase.
    """)
    # Add more sections similarly to the Jira Waterfall guide

# Display the guide based on user selection
display_guide(tool, methodology)

# Footer
st.sidebar.info("This app provides guidelines and best practices for project management tools.")
