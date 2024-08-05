import streamlit as st
import boto3
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# AWS Credentials
aws_region = st.text_input("AWS Region", "us-west-2")
aws_access_key_id = st.text_input("AWS Access Key ID", type="password")
aws_secret_access_key = st.text_input("AWS Secret Access Key", type="password")

# Initialize Boto3 clients
def initialize_clients():
    return {
        "athena": boto3.client('athena', region_name=aws_region, 
                                aws_access_key_id=aws_access_key_id, 
                                aws_secret_access_key=aws_secret_access_key),
        "glue": boto3.client('glue', region_name=aws_region, 
                             aws_access_key_id=aws_access_key_id, 
                             aws_secret_access_key=aws_secret_access_key),
        "redshift": boto3.client('redshift-data', region_name=aws_region, 
                                 aws_access_key_id=aws_access_key_id, 
                                 aws_secret_access_key=aws_secret_access_key),
        "ec2": boto3.client('ec2', region_name=aws_region, 
                            aws_access_key_id=aws_access_key_id, 
                            aws_secret_access_key=aws_secret_access_key),
        "guardduty": boto3.client('guardduty', region_name=aws_region, 
                                   aws_access_key_id=aws_access_key_id, 
                                   aws_secret_access_key=aws_secret_access_key),
    }

# Athena Query Execution
def query_athena(database, query):
    client = initialize_clients()["athena"]
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': 's3://your-query-results-bucket/'}
    )
    query_execution_id = response['QueryExecutionId']
    return query_execution_id

def get_athena_results(query_execution_id):
    client = initialize_clients()["athena"]
    result = client.get_query_results(QueryExecutionId=query_execution_id)
    rows = result['ResultSet']['Rows']
    return pd.DataFrame([r['Data'] for r in rows[1:]], columns=[c['VarCharValue'] for c in rows[0]['Data']])

# Redshift Query Execution
def query_redshift(query):
    conn_str = st.text_input("Redshift Connection String", type="password")
    engine = create_engine(conn_str)
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# MySQL Aurora Query Execution
def query_mysql(query):
    conn_str = st.text_input("MySQL Aurora Connection String", type="password")
    engine = create_engine(conn_str)
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Glue Data Lineage
def get_glue_data_lineage(database):
    client = initialize_clients()["glue"]
    response = client.get_table(DatabaseName=database, Name="your-table-name")
    return response

# EC2 Instance Status
def get_ec2_status():
    client = initialize_clients()["ec2"]
    response = client.describe_instances()
    instances = response['Reservations'][0]['Instances']
    return pd.DataFrame([{
        'InstanceId': i['InstanceId'],
        'InstanceType': i['InstanceType'],
        'State': i['State']['Name']
    } for i in instances])

# GuardDuty Findings
def get_guardduty_findings():
    client = initialize_clients()["guardduty"]
    response = client.list_findings(DetectorId='your-detector-id')
    return response

# Main App Interface
st.title("AWS Services Dashboard")

if aws_access_key_id and aws_secret_access_key:
    st.header("Query Athena")
    database = st.text_input("Athena Database")
    query = st.text_area("Athena Query")
    if st.button("Execute Athena Query"):
        execution_id = query_athena(database, query)
        st.write(f"Query Execution ID: {execution_id}")
        results = get_athena_results(execution_id)
        st.write(results)

    st.header("Query Redshift")
    redshift_query = st.text_area("Redshift Query")
    if st.button("Execute Redshift Query"):
        redshift_results = query_redshift(redshift_query)
        st.write(redshift_results)

    st.header("Query MySQL Aurora")
    mysql_query = st.text_area("MySQL Aurora Query")
    if st.button("Execute MySQL Aurora Query"):
        mysql_results = query_mysql(mysql_query)
        st.write(mysql_results)

    st.header("AWS Glue Data Lineage")
    glue_database = st.text_input("Glue Database")
    if st.button("Get Glue Data Lineage"):
        lineage_info = get_glue_data_lineage(glue_database)
        st.write(lineage_info)

    st.header("EC2 Instance Status")
    if st.button("Get EC2 Status"):
        ec2_status = get_ec2_status()
        st.write(ec2_status)

    st.header("GuardDuty Findings")
    if st.button("Get GuardDuty Findings"):
        findings = get_guardduty_findings()
        st.write(findings)

else:
    st.warning("Please enter AWS credentials")

# Best Practices and Optimization Tips
st.header("Best Practices and Optimization Tips")

st.write("""
### General Tips
- **GuardDuty**: Regularly monitor GuardDuty findings and set up alerts for high-severity issues.
- **IAM Roles**: Ensure IAM roles have the minimal permissions required.
- **VPC/Security Groups**: Implement strict security group rules and use VPCs for isolation.
- **Cost Management**: Use AWS Cost Explorer to keep track of costs and optimize resource usage.

### Informatica Cloud Services (IICS) ETL
#### Staging Layer
- **Data Validation**: Implement validation checks to ensure data integrity.
- **Data Partitioning**: Use partitioning to manage large datasets efficiently.
- **Error Handling**: Incorporate robust error handling and logging.

#### Sanitize Layer
- **Data Cleansing**: Apply rules to clean and standardize data (e.g., remove duplicates, handle missing values).
- **Data Transformation**: Use transformation functions to convert data into the desired format.
- **Performance Optimization**: Optimize transformations for speed and efficiency.

#### Conform Layer
- **Data Integration**: Ensure consistency across different data sources and integrate data into a unified format.
- **Data Quality Checks**: Implement data quality rules to ensure accuracy and completeness.
- **Metadata Management**: Maintain metadata to track data lineage and transformations.

### Optimization Strategies
- **Pushdown Optimization**: Use pushdown optimization in IICS to execute transformations at the source database level to reduce data movement.
- **Incremental Loads**: Use incremental loads to process only new or changed data, reducing the amount of data processed.
- **Parallel Processing**: Utilize parallel processing to handle large volumes of data more efficiently.
- **Resource Tuning**: Monitor and adjust resource allocation based on workload and performance metrics.
""")

st.write("""
### Staging Layer (File Source to S3 Target)
- **File Format**: Use optimized file formats such as Parquet or ORC for efficient storage and querying in S3.
- **Compression**: Apply compression to reduce storage costs and improve read/write performance.
- **Partitioning**: Partition files based on logical criteria (e.g., date, region) to enhance query performance and manageability.
- **Error Handling**: Implement error handling to manage issues during file ingestion, such as missing or corrupted files.
""")

st.write("""
### Sanitize Layer (S3 Source to S3 Target with Different Buckets/Paths)
- **Data Integrity**: Implement validation checks to ensure data consistency between source and target S3 buckets.
- **Data Governance**: Use metadata and data cataloging to manage and track data across different S3 paths.
- **Path Management**: Clearly define and document source and target paths to avoid confusion and ensure smooth data flows.
- **Performance**: Optimize transformations by reducing data movement and processing data in batches.
""")

st.write("""
### Conform Layer (S3 to Redshift and Aurora MySQL)
- **Data Loading**: Use Amazon Redshift Spectrum or COPY command to load data efficiently from S3 into Redshift.
- **Data Transformation**: Perform data transformations in Redshift to leverage its powerful processing capabilities and reduce data movement.
- **Indexing**: Create indexes on Redshift tables to improve query performance.
- **Data Consistency**: Ensure consistency and accuracy of data loaded into Redshift and Aurora MySQL by implementing integrity checks and validation rules.
""")

st.write("""
### Informatica Cloud Services (IICS) Workflows and Scheduling
- **Workflow Design**: Design workflows with modularity and reusability in mind to simplify maintenance and scaling.
- **Error Handling**: Implement comprehensive error handling and alerting mechanisms to manage failures effectively.
- **Scheduling**: Use scheduling to automate data workflows and manage dependencies. Implement retry logic to handle transient failures.
- **Monitoring**: Regularly monitor workflow performance and logs to identify and address bottlenecks or issues.
""")

st.write("""
### Performance Tuning and Parallel Runs
- **Parallel Execution**: Leverage parallel processing to handle large volumes of data efficiently. Configure workflows and tasks to run concurrently where possible.
- **Resource Allocation**: Adjust resource settings based on workload requirements to ensure optimal performance.
- **Data Partitioning**: Partition data during processing to improve performance and scalability.
- **Optimized Queries**: Optimize queries and transformations to reduce execution time and resource consumption.
- **Load Balancing**: Distribute processing across multiple nodes or clusters to balance the load and avoid performance degradation.
""")

st.write("""
### Additional Tips
- **GuardDuty**: Regularly review and address findings related to data access and security.
- **Security Best Practices**: Ensure encryption at rest and in transit for all data stored in S3 and processed in Redshift and Aurora MySQL.
- **Cost Management**: Monitor and manage costs associated with data storage and processing using AWS Cost Explorer and budgeting tools.
""")


st.write("""
### Automate IICS Deployment
- **Infrastructure as Code (IaC)**: Use tools like Terraform or AWS CloudFormation to automate the setup and management of your IICS infrastructure.
- **CI/CD Pipelines**: Integrate IICS deployment into CI/CD pipelines using tools like Jenkins, GitLab CI, or AWS CodePipeline to automate testing and deployment processes.
- **Version Control**: Store IICS configurations and mappings in version control systems like Git to track changes and manage deployments effectively.
- **Automated Testing**: Implement automated testing for your IICS workflows to ensure they perform as expected before deployment.
- **Rollback Strategies**: Have rollback procedures in place to revert to previous configurations in case of deployment failures.
""")

st.write("""
### IICS Infrastructure Setup
- **Scalability**: Design your infrastructure to scale horizontally by adding more nodes or instances as needed to handle increasing data volumes.
- **High Availability**: Implement high availability configurations to ensure your IICS environment is resilient to failures.
- **Network Configuration**: Ensure proper network configurations, including VPC settings and security groups, to allow secure and efficient communication between IICS components and AWS services.
- **Resource Allocation**: Allocate sufficient resources (CPU, memory, storage) based on expected workloads to avoid performance bottlenecks.
- **Monitoring**: Set up monitoring and alerting for your IICS infrastructure to proactively identify and address issues.
""")

st.write("""
### Load Balancing: Distribute Processing Across Multiple Nodes or Clusters
- **Load Balancers**: Use load balancers to distribute incoming requests and data processing tasks evenly across multiple nodes or clusters.
- **Auto-scaling**: Configure auto-scaling policies to automatically adjust the number of instances or nodes based on current load and performance metrics.
- **Data Partitioning**: Partition data to ensure balanced processing and avoid bottlenecks by distributing data across nodes or clusters.
- **Resource Utilization**: Monitor and adjust resource allocation to ensure efficient utilization and prevent overloading specific nodes.
- **Failover Mechanisms**: Implement failover strategies to handle node failures gracefully and maintain uninterrupted processing.
- **Performance Tuning**: Continuously tune load balancing configurations and resource settings based on performance metrics and workload patterns.
""")

st.write("""
### IICS Security Best Practices
- **Data Encryption**: Ensure that all data at rest and in transit is encrypted using strong encryption algorithms. Use AWS KMS or other encryption services as needed.
- **Access Controls**: Implement strict access controls using IAM roles and policies to restrict access to IICS resources and data. Follow the principle of least privilege.
- **Audit Logs**: Enable and regularly review audit logs to track access and changes to IICS resources. Use these logs to detect and respond to unauthorized activities.
- **Secure Communication**: Use secure communication protocols (e.g., HTTPS) for data transfers between IICS and other systems.
- **Network Security**: Ensure proper network security configurations, such as VPC settings and security groups, to protect IICS components and data.
- **User Authentication**: Implement strong authentication mechanisms for IICS users, including multi-factor authentication (MFA) where possible.
- **Regular Updates**: Keep IICS components and related software up to date with the latest security patches and updates.
""")

st.write("""
### Cost Management for IICS Mappings and Workflows
- **Resource Monitoring**: Regularly monitor the usage and performance of IICS mappings and workflows to identify and manage cost drivers. Use AWS Cost Explorer and CloudWatch for insights.
- **Cost Allocation Tags**: Use cost allocation tags to categorize and track costs associated with different mappings, workflows, and projects.
- **Optimization**: Optimize mappings and workflows to reduce resource consumption. Use best practices for efficient data processing, such as minimizing unnecessary transformations and avoiding data redundancy.
- **Scheduled Runs**: Schedule workflows to run during off-peak hours if possible, to take advantage of lower costs and reduce peak-hour resource usage.
- **Budget Alerts**: Set up budget alerts to notify you when spending approaches or exceeds predefined thresholds. This helps in proactively managing costs.
- **Cost Allocation**: Allocate costs to specific projects or departments to better understand and control spending across different areas of your organization.
- **Review and Adjust**: Regularly review and adjust your IICS usage and configurations to align with your budget and performance requirements.
""")

# IICS Performance Tuning for Mapping Design Transformations
st.write("""
### IICS Performance Tuning for Mapping Design Transformations
- **Optimize Transformations**: Use built-in transformations efficiently. Avoid unnecessary transformations and complex logic that can slow down processing.
- **Data Filtering**: Apply filters early in the transformation process to reduce the volume of data being processed.
- **Caching**: Use caching to improve performance for frequently used transformations or lookups.
- **Join Optimization**: Optimize joins by using indexed columns and reducing the size of the datasets being joined.
- **Batch Processing**: Process data in batches to improve performance and manage large volumes more effectively.
- **Minimize Data Movement**: Reduce data movement between different components or stages to enhance performance.
- **Pre-aggregation**: Pre-aggregate data when possible to reduce the amount of processing required during transformations.
- **Profiling and Tuning**: Regularly profile and tune mappings to identify and address performance issues. Use IICS profiling tools to analyze and optimize mapping performance.
""")

st.write("""
### Optimizing Compute Utilization: Multi-Node Environment

#### Source
- **Data Distribution**: Distribute data across nodes to balance the load and prevent any single node from becoming a bottleneck. Use partitioning strategies to achieve this.
- **Efficient Data Extraction**: Use efficient extraction methods to minimize the amount of data read and processed. Apply filters and push down predicates to the source database where possible.

#### Transformations
- **Parallel Processing**: Utilize parallel processing capabilities to run transformations concurrently across multiple nodes. Optimize transformation logic to minimize dependencies and contention.
- **Resource Allocation**: Allocate resources (CPU, memory) based on the complexity and requirements of the transformation tasks. Monitor resource usage and adjust as needed.
- **Optimize Algorithms**: Use optimized algorithms and transformation functions to reduce computational overhead and improve performance.

#### Target
- **Efficient Data Loading**: Use bulk loading techniques and appropriate data formats (e.g., Parquet) to speed up data loading into target systems. Implement batch processing to handle large volumes efficiently.
- **Load Balancing**: Distribute data loading tasks across multiple nodes to balance the workload and improve throughput. Configure target systems to handle parallel writes effectively.

#### Workflow Tasks
- **Task Parallelism**: Design workflows to maximize parallelism by running tasks concurrently where possible. Avoid serial dependencies that can delay overall processing.
- **Resource Management**: Allocate sufficient resources for workflow tasks to ensure they run efficiently. Monitor and adjust based on workload and performance metrics.

#### Command Tasks
- **Optimize Command Execution**: Ensure that command tasks are optimized for performance. Use efficient scripts and commands to minimize execution time.
- **Asynchronous Execution**: Run command tasks asynchronously when possible to prevent them from blocking other workflow tasks and to improve overall throughput.

#### General Tips
- **Monitoring and Tuning**: Continuously monitor compute utilization and performance metrics. Use tools to identify bottlenecks and adjust configurations accordingly.
- **Auto-scaling**: Implement auto-scaling policies to dynamically adjust the number of nodes based on current workload and performance needs.
- **Load Testing**: Conduct load testing to ensure that your multi-node setup can handle peak loads and to fine-tune resource allocation.

""")








