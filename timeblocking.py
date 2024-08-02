import streamlit as st
import pandas as pd
import datetime

# Initial Task Data
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add task
def add_task(task, priority, due_date, start_time, end_time):
    task_dict = {
        'Task': task,
        'Priority': priority,
        'Due Date': due_date,
        'Start Time': start_time,
        'End Time': end_time,
        'Completed': False
    }
    st.session_state.tasks.append(task_dict)

# Function to complete task
def complete_task(task_index):
    st.session_state.tasks[task_index]['Completed'] = True

# Function to delete task
def delete_task(task_index):
    del st.session_state.tasks[task_index]

# Custom CSS for Button Styling
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    .completed-task {
        text-decoration: line-through;
        color: gray;
    }
    .stButton>button {
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        margin: 5px;
    }
    .stButton>button.complete-button {
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button.delete-button {
        background-color: #f44336;
        color: white;
    }
    .stButton>button:hover {
        opacity: 0.8;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for Task Input
st.sidebar.title("Add New Task")
with st.sidebar.form(key='task_form'):
    task = st.text_input("Task")
    priority = st.selectbox("Priority", ["Urgent", "Important", "Not Urgent", "Not Important"])
    due_date = st.date_input("Due Date", datetime.date.today())
    start_time = st.time_input("Start Time", datetime.time(9, 0))
    end_time = st.time_input("End Time", datetime.time(10, 0))
    submit_button = st.form_submit_button(label='Add Task')

if submit_button and task:
    add_task(task, priority, due_date, start_time, end_time)
    st.sidebar.success("Task added successfully!")

# Main App Layout
st.title("Time Management App")

# Display Tasks in Columns
st.subheader("Task List")
for index, task in enumerate(st.session_state.tasks):
    col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 3])
    task_text = f"<p class='{'completed-task' if task['Completed'] else ''}'>{task['Task']}</p>"
    col1.markdown(task_text, unsafe_allow_html=True)
    col2.write(task['Priority'])
    col3.write(task['Due Date'])
    col4.write(task['Start Time'])
    col5.write(task['End Time'])
    
    # Display buttons in the last column
    with col6:
        if not task['Completed']:
            st.button("Complete", key=f"complete_{index}", on_click=complete_task, args=(index,), help="Mark task as completed", use_container_width=True)
        st.button("Delete", key=f"delete_{index}", on_click=delete_task, args=(index,), help="Delete task", use_container_width=True)

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

# Custom Footer
st.markdown("<hr><p class='big-font'>Streamlit Time Management App</p>", unsafe_allow_html=True)
