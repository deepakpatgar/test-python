import streamlit as st
import pandas as pd
import datetime

# Task Data
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add task
def add_task(task, priority, due_date):
    task_dict = {'Task': task, 'Priority': priority, 'Due Date': due_date, 'Completed': False}
    st.session_state.tasks.append(task_dict)

# Function to complete task
def complete_task(task_index):
    st.session_state.tasks[task_index]['Completed'] = True

# Function to delete task
def delete_task(task_index):
    del st.session_state.tasks[task_index]

# Streamlit UI
st.title("Time Management App")

# Input form for adding a new task
with st.form(key='task_form'):
    task = st.text_input("Task")
    priority = st.selectbox("Priority", ["Urgent", "Important", "Not Urgent", "Not Important"])
    due_date = st.date_input("Due Date", datetime.date.today())
    submit_button = st.form_submit_button(label='Add Task')

if submit_button and task:
    add_task(task, priority, due_date)
    st.success("Task added successfully!")

# Display tasks
st.subheader("Task List")
for index, task in enumerate(st.session_state.tasks):
    col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
    col1.write(task['Task'])
    col2.write(task['Priority'])
    col3.write(task['Due Date'])
    if task['Completed']:
        col4.write("Completed")
    else:
        if col4.button("Complete", key=f"complete_{index}"):
            complete_task(index)
        if col4.button("Delete", key=f"delete_{index}"):
            delete_task(index)

# Pomodoro Timer
st.subheader("Pomodoro Timer")
if st.button('Start Pomodoro'):
    st.session_state.pomodoro_start = datetime.datetime.now()

if 'pomodoro_start' in st.session_state:
    elapsed_time = datetime.datetime.now() - st.session_state.pomodoro_start
    st.write(f"Elapsed Time: {elapsed_time.seconds // 60} minutes {elapsed_time.seconds % 60} seconds")

# Statistics
st.subheader("Statistics")
completed_tasks = [task for task in st.session_state.tasks if task['Completed']]
st.write(f"Total Tasks: {len(st.session_state.tasks)}")
st.write(f"Completed Tasks: {len(completed_tasks)}")

# Visualization
if completed_tasks:
    df = pd.DataFrame(st.session_state.tasks)
    st.bar_chart(df['Priority'].value_counts())
