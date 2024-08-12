import streamlit as st

# Define a function to display best practices for each type of app
def display_best_practices(app_type):
    if app_type == "Streamlit App":
        st.subheader("Best Practices for Streamlit App")
        st.markdown("""
        - **Folder Structure:**
            - Separate business logic, configuration, and presentation layers.
            - Example:
            ```
            ├── app.py
            ├── pages/
            │   ├── page1.py
            │   ├── page2.py
            ├── assets/
            │   ├── images/
            │   ├── css/
            ├── components/
            │   ├── header.py
            │   ├── footer.py
            ├── utils/
            │   ├── helpers.py
            │   ├── config.py
            ├── data/
            │   ├── data_source.csv
            └── requirements.txt
            ```
        - **Nomenclature:**
            - Use clear and descriptive names for components (e.g., `header.py` for the header section).
            - Follow consistent naming conventions for files, variables, and functions.
        - **Security:**
            - Use HTTPS for all deployments to secure data transmission.
            - Implement user authentication and authorization if handling sensitive data.
        - **Performance Optimization:**
            - Cache heavy computations and data fetching using `@st.cache_data` or `@st.cache_resource`.
            - Optimize image and asset loading by using appropriate formats and sizes.
        - **Guardrails:**
            - Ensure compatibility with different screen sizes and browsers.
            - Validate and sanitize all user inputs.
        - **Testing:**
            - Write unit and integration tests for critical components using frameworks like `pytest`.
        - **Version Control:**
            - Use a `.gitignore` file to exclude unnecessary files from version control (e.g., data files, local configuration).
        - **Important Tips:**
            - Document your code thoroughly with comments and a `README.md` file.
            - Use custom themes and CSS for better UI/UX.
        """)

    elif app_type == "Flask App":
        st.subheader("Best Practices for Flask App")
        st.markdown("""
        - **Folder Structure:**
            - Modularize the app by separating routes, models, and views.
            - Example:
            ```
            ├── app/
            │   ├── __init__.py
            │   ├── routes.py
            │   ├── models.py
            │   ├── forms.py
            │   ├── static/
            │   │   ├── css/
            │   │   ├── js/
            │   ├── templates/
            │   │   ├── index.html
            ├── config.py
            ├── migrations/
            ├── instance/
            ├── tests/
            ├── run.py
            └── requirements.txt
            ```
        - **Nomenclature:**
            - Use RESTful naming conventions for routes (e.g., `/users/create`).
            - Name HTML templates descriptively (e.g., `user_profile.html`).
        - **Security:**
            - Implement CSRF protection and use secure cookies.
            - Validate and sanitize all user inputs to prevent injection attacks.
            - Use environment variables to store sensitive information (e.g., `FLASK_SECRET_KEY`).
        - **Performance Optimization:**
            - Use caching (e.g., Flask-Caching) for frequently accessed data.
            - Optimize database queries by using indexing and query optimization techniques.
        - **Guardrails:**
            - Implement error handling with custom error pages.
            - Ensure proper logging of errors and requests.
        - **Testing:**
            - Write unit tests for views, models, and forms.
            - Use Flask’s testing client for integration tests.
        - **Version Control:**
            - Exclude database files and instance folders from version control using `.gitignore`.
        - **Important Tips:**
            - Use blueprints to structure larger applications into manageable components.
            - Maintain a clear and up-to-date `README.md` with setup instructions.
        """)

    elif app_type == "Gradio App":
        st.subheader("Best Practices for Gradio App")
        st.markdown("""
        - **Folder Structure:**
            - Organize assets, scripts, and models in a logical manner.
            - Example:
            ```
            ├── app.py
            ├── components/
            ├── assets/
            │   ├── images/
            │   ├── models/
            ├── data/
            ├── notebooks/
            ├── tests/
            └── requirements.txt
            ```
        - **Nomenclature:**
            - Use descriptive names for inputs, outputs, and components.
            - Follow consistent naming conventions (e.g., `input_image`, `output_label`).
        - **Security:**
            - Secure file uploads by checking file types and limiting file sizes.
            - Avoid exposing sensitive information through the UI or logs.
        - **Performance Optimization:**
            - Use lightweight models and pre-process inputs to reduce load times.
            - Optimize asset loading by using appropriate formats and sizes.
        - **Guardrails:**
            - Test the app on different browsers and devices to ensure compatibility.
            - Validate all user inputs to prevent malicious inputs.
        - **Testing:**
            - Write unit tests for your components using frameworks like `unittest` or `pytest`.
        - **Version Control:**
            - Track model versions and document changes in a `changelog.md`.
        - **Important Tips:**
            - Use Gradio's built-in deployment tools or integrate with other deployment platforms (e.g., Hugging Face Spaces).
            - Keep your app modular for easier maintenance and scalability.
        """)

    elif app_type == "UNIX Script-Driven App":
        st.subheader("Best Practices for UNIX Script-Driven App")
        st.markdown("""
        - **Folder Structure:**
            - Organize scripts based on functionality and maintain clear documentation.
            - Example:
            ```
            ├── bin/
            │   ├── data_processing.sh
            │   ├── backup.sh
            ├── logs/
            │   ├── app.log
            ├── config/
            │   ├── app.conf
            └── README.md
            ```
        - **Nomenclature:**
            - Use clear, descriptive names for scripts (e.g., `backup.sh`).
            - Follow a consistent naming convention (e.g., lowercase with underscores).
        - **Security:**
            - Set appropriate file permissions (e.g., `chmod 700` for sensitive scripts).
            - Avoid storing passwords or sensitive information in scripts; use environment variables or configuration files.
        - **Performance Optimization:**
            - Write efficient code by minimizing unnecessary loops and optimizing command usage.
            - Use background processes (`&`) for long-running tasks.
        - **Guardrails:**
            - Implement error handling using `set -e` and provide meaningful error messages.
            - Ensure proper logging of script activities for auditing.
        - **Testing:**
            - Test scripts in a safe environment before deploying to production.
            - Use shellcheck to identify common scripting errors.
        - **Version Control:**
            - Use version control to track changes in scripts, especially if multiple users are involved.
        - **Important Tips:**
            - Regularly review and clean up old or unused scripts.
            - Document each script’s purpose, usage, and parameters in the `README.md`.
        """)

    elif app_type == "Python Script-Driven App":
        st.subheader("Best Practices for Python Script-Driven App")
        st.markdown("""
        - **Folder Structure:**
            - Structure scripts, data, and modules logically.
            - Example:
            ```
            ├── main.py
            ├── modules/
            │   ├── data_processing.py
            │   ├── utils.py
            ├── data/
            │   ├── input_data.csv
            │   ├── output_data.csv
            ├── tests/
            │   ├── test_data_processing.py
            └── requirements.txt
            ```
        - **Nomenclature:**
            - Use snake_case for file names, functions, and variables.
            - Choose descriptive names that reflect the function's or file's purpose.
        - **Security:**
            - Use virtual environments to isolate dependencies.
            - Avoid hard-coding sensitive data like API keys; use environment variables instead.
        - **Performance Optimization:**
            - Profile your code using tools like `cProfile` to identify bottlenecks.
            - Use generators and list comprehensions for memory efficiency.
        - **Guardrails:**
            - Implement error handling using `try-except` blocks and ensure your code is portable across environments.
            - Write modular code to enhance reusability and maintainability.
        - **Testing:**
            - Write unit tests for each function and module using `unittest` or `pytest`.
            - Automate tests using CI/CD pipelines.
        - **Version Control:**
            - Document your commit messages clearly and follow a consistent style (e.g., Conventional Commits).
            - Use `.gitignore` to exclude unnecessary files (e.g., data, environment files) from version control.
        - **Important Tips:**
            - Implement logging for better debugging and monitoring.
            - Maintain up-to-date documentation for your scripts and modules.
        """)

# Streamlit app layout
st.title("App Development Best Practices Guide")

st.markdown("""
This application provides best practices, guardrails, security guidelines, folder structure standards, nomenclature, and important tips for developing various types of applications.
""")

# Dropdown menu for selecting the type of app
app_type = st.selectbox("Select the type of app:", 
                        ["Streamlit App", "Flask App", "Gradio App", "UNIX Script-Driven App", "Python Script-Driven App"])

# Display best practices based on the selected app type
display_best_practices(app_type)

# Optional additional sections
st.markdown("### General Security Best Practices")
st.markdown("""
- **Dependency Management:** Regularly update dependencies and monitor for security vulnerabilities using tools like `pip-audit`.
- **Environment Variables:** Use `.env` files or environment variables to store sensitive data, and never hard-code sensitive information in your scripts.
- **Access Control:** Limit access to production environments and use role-based access control (RBAC) where possible.
- **Logging:** Implement logging at different levels (INFO, WARNING, ERROR) to monitor application behavior and detect anomalies.
- **Monitoring:** Use monitoring tools (e.g., Prometheus, Grafana) to track application performance and health.
- **Encryption:** Encrypt sensitive data at rest and in transit.
- **Code Review:** Conduct regular code reviews to identify potential security issues and ensure adherence to best practices.
""")

st.markdown("### General Folder Structure Tips")
st.markdown("""
- **Modularity:** Break down your application into modules to improve maintainability and readability.
- **Separation of Concerns:** Keep business logic, data access, and presentation layers separate.
- **Configuration Files:** Store configuration in a dedicated folder (e.g., `config/`) and use environment-specific configurations (e.g., `config/dev.yaml`, `config/prod.yaml`).
- **Documentation:** Include a `docs/` folder with detailed documentation, including setup instructions, API references, and usage examples.
- **Assets Management:** Keep all static assets (e.g., images, CSS, JavaScript) in an `assets/` or `static/` folder for easy management.
- **Data Management:** Store raw data, processed data, and outputs in separate folders (e.g., `data/raw/`, `data/processed/`, `data/output/`).
""")

st.markdown("### General Nomenclature Tips")
st.markdown("""
- **Consistency:** Maintain consistent naming conventions throughout the codebase.
- **Clarity:** Use descriptive names that convey the purpose and function of the component, variable, or file.
- **Avoid Abbreviations:** Unless commonly accepted, avoid using abbreviations in names to reduce ambiguity.
- **Case Style:** 
    - Use `snake_case` for functions, variables, and file names.
    - Use `CamelCase` for class names.
    - Use `UPPER_SNAKE_CASE` for constants.
- **Naming Conventions for Scripts:**
    - Prefix scripts with verbs that indicate their action (e.g., `generate_report.py`, `process_data.sh`).
""")

st.markdown("### General Testing Best Practices")
st.markdown("""
- **Unit Testing:** Write unit tests for individual functions and modules to ensure they behave as expected.
- **Integration Testing:** Test how different parts of your application work together.
- **End-to-End Testing:** Simulate real user scenarios to ensure the entire application works as intended.
- **Test Coverage:** Aim for high test coverage, but focus on testing critical and complex parts of the application.
- **Continuous Integration:** Use CI/CD pipelines to automate testing and deployment processes.
- **Test Data Management:** Use realistic test data and store it in a dedicated folder (e.g., `tests/data/`).
""")

st.markdown("### General Deployment Tips")
st.markdown("""
- **Environment Management:** Use virtual environments (e.g., `venv`, `virtualenv`) to manage dependencies and avoid conflicts.
- **Deployment Automation:** Use tools like Docker, Terraform, or Ansible to automate deployment processes.
- **Versioning:** Implement version control for deployments to keep track of different versions of your application.
- **Rollback Strategy:** Plan for rollback strategies in case a deployment fails.
- **Monitoring and Alerts:** Set up monitoring and alerting mechanisms to ensure that you are notified of any issues post-deployment.
- **Backup:** Regularly backup critical data and configurations before deploying new changes.
""")

st.markdown("### Debugging Guidelines")
st.markdown("""
- **Streamlit App:**
    - Use `st.write()` and `st.debug()` to print variables and intermediate results to the sidebar.
    - Utilize Streamlit’s built-in error messages to quickly identify issues.
    - Use the `--log_level=debug` flag when running the app to see detailed logs.
- **Flask App:**
    - Use Flask’s built-in `debug=True` mode to get detailed error pages.
    - Integrate Python’s `logging` module to log errors and debug information to files.
    - Employ breakpoints (`import pdb; pdb.set_trace()`) for step-by-step debugging.
- **Gradio App:**
    - Use Gradio’s `debug=True` flag to get detailed logs.
    - Print intermediate results to the console for easy debugging.
    - Use Python debuggers like `pdb` or IDE-based debuggers for in-depth debugging.
- **UNIX Script-Driven App:**
    - Use `set -x` to enable a trace of simple commands and their arguments.
    - Use `echo` statements to print variable values and script progress.
    - Review logs in the `logs/` directory to identify errors and issues.
- **Python Script-Driven App:**
    - Use `logging` for capturing detailed debug information.
    - Implement `try-except` blocks to handle and log exceptions.
    - Utilize debuggers like `pdb` or IDE-based debugging tools for in-depth analysis.
""")

st.markdown("### Unit Testing and Testing Guidelines")
st.markdown("""
- **Streamlit App:**
    - Use `pytest` to write unit tests for individual components.
    - Mock Streamlit functions and user inputs for isolated testing.
    - Test data processing logic separately from the UI.
- **Flask App:**
    - Write unit tests for views, models, and forms using `unittest` or `pytest`.
    - Use Flask’s test client to simulate requests and validate responses.
    - Mock external dependencies like databases and APIs to isolate test cases.
- **Gradio App:**
    - Write unit tests for Gradio interface components.
    - Use mocking for any external API calls or file operations.
    - Ensure test coverage for all input and output scenarios.
- **UNIX Script-Driven App:**
    - Use shell testing frameworks like `bats` to write tests for shell scripts.
    - Validate script outputs and side effects (e.g., file creation, data processing).
    - Test scripts in isolated environments to avoid side effects on production data.
- **Python Script-Driven App:**
    - Use `pytest` or `unittest` for comprehensive test coverage.
    - Mock external dependencies and side effects (e.g., file I/O, network calls).
    - Write parameterized tests for functions that accept various inputs.
""")

st.markdown("### Documentation for Deliverables")
st.markdown("""
- **Project Overview Document:**
    - Summary of the project, objectives, scope, and deliverables.
    - High-level architecture diagram and explanation.
- **Installation Guide:**
    - Step-by-step instructions for setting up the application, including dependencies, environment setup, and configuration.
    - Information on how to deploy the application (locally and in production).
- **User Manual:**
    - Detailed guide on how to use the application, including screenshots and examples.
    - Explanation of key features and functionality.
- **Developer Guide:**
    - Detailed explanation of the codebase structure and key components.
    - Instructions for setting up a development environment, including tools and dependencies.
    - Guidelines for contributing to the project (e.g., coding standards, branching strategy).
- **Testing Report:**
    - Summary of all tests performed, including unit tests, integration tests, and end-to-end tests.
    - Test coverage report and details of any known issues.
- **Release Notes:**
    - Documentation of each version, including new features, bug fixes, and improvements.
    - Version history and changelog.
- **Backup and Recovery Plan:**
    - Detailed procedures for backing up application data and configuration.
    - Instructions for restoring the application in case of failure.
- **Security Guidelines:**
    - Documentation of all security measures implemented in the application.
    - Guidelines for maintaining security during operation and updates.
""")



