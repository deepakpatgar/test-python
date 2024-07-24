import streamlit as st
import subprocess

# Function to check if a command is successful
def check_command(command):
    try:
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to display connection status
def display_status(tool, status):
    if status:
        st.success(f"{tool} is configured and running.")
    else:
        st.error(f"{tool} is not configured or not running.")

# Main Streamlit app
def main():
    st.title("Tool Configuration and Status Checker")
    st.write("Guide and configure various tools, then check their connection status.")

    # Create columns for side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Apache Airflow")
        st.write("Setup and configure Apache Airflow")
        if st.button("Configure Airflow"):
            status = check_command("airflow version")
            display_status("Apache Airflow", status)

        st.subheader("GitHub")
        st.write("Setup and configure GitHub")
        if st.button("Configure GitHub"):
            status = check_command("git --version")
            display_status("GitHub", status)

        st.subheader("JIRA")
        st.write("Setup and configure JIRA")
        if st.button("Configure JIRA"):
            status = check_command("jira --version")
            display_status("JIRA", status)

        st.subheader("PySpark")
        st.write("Setup and configure PySpark")
        if st.button("Configure PySpark"):
            status = check_command("pyspark --version")
            display_status("PySpark", status)

        st.subheader("WSL")
        st.write("Setup and configure WSL")
        if st.button("Configure WSL"):
            status = check_command("wsl --status")
            display_status("WSL", status)

        st.subheader("MS Teams")
        st.write("Setup and configure MS Teams")
        if st.button("Configure MS Teams"):
            status = check_command("teams --version")
            display_status("MS Teams", status)

    with col2:
        st.subheader("Jenkins")
        st.write("Setup and configure Jenkins")
        if st.button("Configure Jenkins"):
            status = check_command("jenkins --version")
            display_status("Jenkins", status)

        st.subheader("Bitbucket")
        st.write("Setup and configure Bitbucket")
        if st.button("Configure Bitbucket"):
            status = check_command("git --version")
            display_status("Bitbucket", status)

        st.subheader("Databases")
        st.write("Setup and configure Databases (MySQL example)")
        if st.button("Configure Database"):
            status = check_command("mysql --version")
            display_status("MySQL Database", status)

        st.subheader("Python")
        st.write("Setup and configure Python")
        if st.button("Configure Python"):
            status = check_command("python --version")
            display_status("Python", status)

        st.subheader("Unix")
        st.write("Setup and configure Unix")
        if st.button("Configure Unix"):
            status = check_command("uname -a")
            display_status("Unix", status)

        st.subheader("Slack")
        st.write("Setup and configure Slack")
        if st.button("Configure Slack"):
            status = check_command("slack --version")
            display_status("Slack", status)

if __name__ == "__main__":
    main()
