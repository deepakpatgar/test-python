import streamlit as st
import snowflake.connector
from snowflake.connector import DictCursor

# Function to create a connection to Snowflake
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user=st.secrets["SNOWFLAKE_USER"],
        password=st.secrets["SNOWFLAKE_PASSWORD"],
        account=st.secrets["SNOWFLAKE_ACCOUNT"],
        warehouse=st.secrets["SNOWFLAKE_WAREHOUSE"],
        database=st.secrets["SNOWFLAKE_DATABASE"],
        schema=st.secrets["SNOWFLAKE_SCHEMA"]
    )
    return conn

# Function to execute a query
def execute_query(query):
    conn = create_snowflake_connection()
    cur = conn.cursor(DictCursor)
    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# Main Streamlit app
st.title("Snowflake Services Interface")

# Sidebar for selecting the service
service = st.sidebar.selectbox(
    "Select Snowflake Service",
    ("Data Warehouse", "Audit Information Store", "Data Query on Staging Layer", "Data Lineage Information")
)

if service == "Data Warehouse":
    st.header("Snowflake Data Warehouse")
    query = st.text_area("Enter your SQL query for the Data Warehouse:")
    if st.button("Execute"):
        results = execute_query(query)
        st.write(results)

elif service == "Audit Information Store":
    st.header("Snowflake Audit Information Store")
    query = st.text_area("Enter your SQL query for the Audit Information Store:")
    if st.button("Execute"):
        results = execute_query(query)
        st.write(results)

elif service == "Data Query on Staging Layer":
    st.header("Snowflake Data Query on Staging Layer")
    query = st.text_area("Enter your SQL query for the Staging Layer:")
    if st.button("Execute"):
        results = execute_query(query)
        st.write(results)

elif service == "Data Lineage Information":
    st.header("Snowflake Data Lineage Information")
    query = st.text_area("Enter your SQL query for Data Lineage:")
    if st.button("Execute"):
        results = execute_query(query)
        st.write(results)

# Best practices and tips

st.write("""
### Best Practices for Snowflake and IICS:

#### IICS ETL Performance:
- **Parallel Processing:** Use concurrent tasks to optimize performance.
- **Bulk API:** Utilize bulk API for large data volumes to improve load times.
- **Error Handling:** Implement robust error handling mechanisms and logging.
- **Data Lineage:** Maintain detailed metadata for data lineage and traceability.
- **Scheduling:** Schedule jobs during off-peak hours to reduce load on the system.

#### Snowflake Security:
- **Roles and Permissions:** Implement role-based access control (RBAC).
- **Encryption:** Ensure data is encrypted both in transit and at rest.
- **Multi-Factor Authentication (MFA):** Enable MFA for all users.
- **Network Policies:** Restrict access through network policies and IP whitelisting.
- **Audit Logging:** Enable and monitor audit logs for suspicious activities.

#### Naming Conventions:
- **Databases:** Use descriptive names that indicate the purpose (e.g., `SALES_DB`, `FINANCE_DB`).
- **Schemas:** Indicate the schema's purpose and context (e.g., `RAW_DATA`, `PROCESSED_DATA`).
- **Tables:** Use clear, concise names that reflect the content (e.g., `CUSTOMERS`, `SALES_TRANSACTIONS`).
- **Layers:** Use consistent abbreviations and prefixes (e.g., `STG_` for staging, `TGT_` for target).

**Examples:**
- Database: `ANALYTICS_DB`
- Schema: `STG_RAW_DATA`
- Table: `STG_CUSTOMERS`
- Table: `TGT_SALES_TRANSACTIONS`

#### Additional Tips:
- **Documentation:** Maintain thorough documentation for all ETL processes and data flows.
- **Version Control:** Use version control for ETL scripts and configurations.
- **Monitoring:** Implement continuous monitoring and alerting for ETL jobs and Snowflake usage.
- **Optimization:** Regularly review and optimize queries, indexes, and data partitioning.

### GuardDuty and Monitoring:
- **GuardDuty:** Set up AWS GuardDuty for real-time monitoring of threats.
- **Audit Logs:** Regularly review and analyze audit logs for unusual activities.

#### Best Practices for Cost Management:
- **Warehouse Sizing:** Right-size your warehouses based on workload requirements; scale up or down as needed.
- **Auto-Suspend & Auto-Resume:** Use auto-suspend and auto-resume settings for warehouses to minimize costs when they are idle.
- **Query Optimization:** Regularly optimize queries to reduce the number of compute resources used.
- **Storage Optimization:** Periodically review and purge outdated data to manage storage costs.
- **Usage Monitoring:** Use Snowflake's built-in usage and billing views to track and forecast costs.
- **Resource Governance:** Implement resource monitors to set spend limits and alerts.

#### Best Practices for ETL & Snowflake Error Handling:
- **Retry Mechanisms:** Implement automatic retries for transient errors in ETL jobs.
- **Transaction Management:** Use Snowflake's transaction control to ensure data consistency and rollback in case of failures.
- **Error Alerts:** Set up notifications and alerts for critical ETL errors.
- **Validation Checks:** Perform data validation checks during the ETL process to catch errors early.
- **Error Logging:** Log all errors with detailed information to facilitate troubleshooting.                 

#### Best Practices for Logging and Auditing:
- **Comprehensive Logging:** Implement logging for all ETL jobs, capturing key details like start and end times, row counts, and errors.
- **Audit Trails:** Maintain audit trails for all data changes, including inserts, updates, and deletes.
- **Regular Reviews:** Schedule regular reviews of logs and audit trails to ensure compliance and spot anomalies.
- **Automated Audits:** Use Snowflake's built-in audit features to automatically track user activity and data access.
- **Data Retention Policies:** Define and enforce data retention policies for logs and audit trails to comply with legal and regulatory requirements.

         #### Best Practices for DDL Standards:

**Flat Files (Parquet):**
- **Consistent Naming:** Use consistent and descriptive naming conventions for Parquet files. Include relevant details like date, source, and data type.
  - Example: `sales_data_2023_08_05.parquet`
- **Partitioning:** Use appropriate partitioning strategies based on query patterns (e.g., partition by date or region).
- **Schema Management:** Ensure schema consistency across Parquet files. Define a schema evolution strategy for handling changes over time.
- **Compression:** Utilize compression (e.g., Snappy, Gzip) to reduce file size and improve query performance.

**ETL Tables:**
- **Naming Conventions:** Use clear and consistent naming conventions for databases, schemas, and tables.
  - Database: `ETL_DB`
  - Schema: `STG_RAW_DATA`, `TGT_PROCESSED_DATA`
  - Tables: `STG_CUSTOMERS`, `TGT_SALES_TRANSACTIONS`
- **Column Naming:** Use meaningful column names and avoid ambiguous abbreviations. Follow a consistent naming style (e.g., snake_case or camelCase).
  - Example: `customer_id`, `sales_amount`
- **Data Types:** Choose appropriate data types for each column. Consider using native data types that Snowflake supports for better performance.
- **Primary Keys and Indexes:** Define primary keys and indexes to ensure data integrity and optimize query performance.
- **Data Governance:** Implement data governance policies to manage data quality, consistency, and security.
- **Metadata Management:** Maintain comprehensive metadata for all ETL tables, including descriptions, data lineage, and transformation rules.

**Stored Procedures:**
- **Naming Conventions:** Use clear and descriptive names for stored procedures.
  - Example: `sp_update_customer_records`
- **Parameter Naming:** Use meaningful names for parameters and specify default values where appropriate.
- **Error Handling:** Implement robust error handling within stored procedures using `TRY...CATCH` blocks.
- **Logging:** Include logging mechanisms to capture execution details, such as start time, end time, and errors.
- **Version Control:** Maintain version control for stored procedures to track changes and revert if necessary.

**Functions:**
- **Scalar Functions:** Use scalar functions for simple computations that return a single value.
  - Example: `fn_calculate_discount`
- **Table Functions:** Use table functions for operations that return a set of rows.
  - Example: `tf_get_sales_data`
- **Performance:** Avoid complex logic within functions that can degrade performance. Offload complex processing to the main query or stored procedures.
- **Reusability:** Write reusable functions that can be called from multiple places within your ETL workflows.

#### Important Tips:
- **Documentation:** Provide comprehensive documentation for stored procedures and functions, including purpose, parameters, and example usage.
- **Security:** Use roles and permissions to control access to stored procedures and functions. Ensure sensitive operations are protected.
- **Testing:** Thoroughly test stored procedures and functions in a development environment before deploying to production.

#### Best Practices for Snowpark:

**Code Management:**
- **Modular Code:** Write modular code for better readability and maintainability. Break down complex logic into smaller, reusable functions.
- **Version Control:** Use version control systems like Git to manage your Snowpark code. Maintain branches for development, testing, and production.

**Performance Optimization:**
- **Data Locality:** Minimize data shuffling by leveraging Snowflake's clustering and partitioning strategies.
- **Lazy Evaluation:** Use lazy evaluation techniques to optimize performance. Avoid unnecessary computations and materializations.
- **Resource Allocation:** Optimize resource allocation by adjusting the size and number of Snowpark sessions based on workload requirements.

**Data Processing:**
- **Schema Enforcement:** Enforce schemas to ensure data consistency and avoid runtime errors.
- **Error Handling:** Implement comprehensive error handling to manage exceptions and ensure robust data processing.
- **Logging and Monitoring:** Integrate logging and monitoring mechanisms to capture execution details and track performance metrics.

**Security:**
- **Role-Based Access Control:** Implement role-based access control (RBAC) to manage permissions for Snowpark sessions and resources.
- **Data Encryption:** Ensure data is encrypted both in transit and at rest. Use Snowflake's built-in encryption features.
- **Compliance:** Adhere to organizational and regulatory compliance requirements when processing data with Snowpark.

#### Important Tips:
- **Documentation:** Provide detailed documentation for your Snowpark code, including explanations of key functions and workflows.
- **Testing:** Implement unit tests and integration tests to validate the functionality and performance of your Snowpark code.
- **Collaboration:** Encourage collaboration among team members by using shared repositories and code review practices.
                  

""")



