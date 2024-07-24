import streamlit as st

def get_aws_redshift_recommendations(node_type, storage_size, query_count):
    recommendations = []
    if node_type.startswith('dc2') and storage_size > 1000:  # Example threshold for DC2 nodes
        recommendations.append("Consider using RA3 nodes for better storage and performance optimization.")
    if query_count > 1000:  # Example threshold for query count
        recommendations.append("Optimize your queries and use workload management (WLM) for better performance.")
    if storage_size > 500:  # Example threshold for storage size in GB
        recommendations.append("Use automatic table optimization and compression to manage storage effectively.")
    return recommendations

def get_aws_aurora_recommendations(instance_class, storage_size, iops):
    recommendations = []
    if instance_class.startswith('db.r5') and storage_size > 1000:  # Example threshold for R5 instances
        recommendations.append("Consider using Aurora Serverless for variable workloads to reduce costs.")
    if iops > 5000:  # Example threshold for IOPS
        recommendations.append("Optimize your database queries and schema to reduce IOPS.")
    if storage_size > 500:  # Example threshold for storage size in GB
        recommendations.append("Enable automatic backups and snapshots to manage storage effectively.")
    return recommendations

def get_aws_athena_recommendations(query_count, data_scanned, cost):
    recommendations = []
    if query_count > 1000:  # Example threshold for query count
        recommendations.append("Partition your data to reduce the amount of data scanned by queries.")
    if data_scanned > 1000:  # Example threshold for data scanned in GB
        recommendations.append("Use columnar data formats like Parquet or ORC to reduce data scanned.")
    if cost > 100:  # Example threshold in USD
        recommendations.append("Optimize queries to reduce costs, and use AWS Glue to catalog data for better performance.")
    return recommendations

def get_aws_efs_recommendations(storage_size, access_frequency, throughput_mode):
    recommendations = []
    if storage_size > 500:  # Example threshold for storage size in GB
        recommendations.append("Use Lifecycle Management to transition infrequently accessed files to the Infrequent Access storage class.")
    if access_frequency < 100:  # Example threshold for low access frequency
        recommendations.append("Consider using the Infrequent Access storage class to reduce costs.")
    if throughput_mode == "provisioned":
        recommendations.append("Review your throughput requirements and consider using Bursting Throughput mode if suitable.")
    return recommendations


def get_apache_airflow_recommendations(concurrency, dag_count, task_duration):
    recommendations = []
    if concurrency > 100:  # Example threshold
        recommendations.append("Increase the number of workers for better performance.")
    if dag_count > 50:  # Example threshold
        recommendations.append("Consider breaking down complex DAGs into smaller ones.")
    if task_duration > 3600:  # Example threshold in seconds
        recommendations.append("Optimize task duration by breaking down into smaller tasks.")
    return recommendations

def get_aws_s3_recommendations(storage_size, duration, cost):
    recommendations = []
    if storage_size > 1000:  # Example threshold in GB
        recommendations.append("Consider using Intelligent-Tiering for cost optimization.")
    if duration > 365:  # Example threshold in days
        recommendations.append("Consider transitioning to Glacier for long-term storage.")
    if cost > 1000:  # Example threshold in USD
        recommendations.append("Review your storage class usage and optimize for cost.")
    return recommendations

def get_aws_ec2_recommendations(instance_type, usage_hours, cost):
    recommendations = []
    if instance_type.startswith('t2.') and usage_hours > 720:  # Example threshold for T2 instances
        recommendations.append("Consider switching to a more suitable instance type for heavy usage.")
    if usage_hours < 100:  # Example threshold for low usage
        recommendations.append("Consider using spot instances for cost savings.")
    if cost > 500:  # Example threshold in USD
        recommendations.append("Review your instance reservations for potential savings.")
    return recommendations

def get_aws_lambda_recommendations(memory_size, duration, invocations):
    recommendations = []
    if memory_size > 1024:  # Example threshold in MB
        recommendations.append("Review memory allocation to ensure it's appropriate for your function.")
    if duration > 300:  # Example threshold in seconds
        recommendations.append("Optimize your code to reduce execution time.")
    if invocations > 1000000:  # Example threshold for invocations
        recommendations.append("Consider using AWS Step Functions for complex workflows.")
    return recommendations

# Define similar functions for other AWS services and tools...

def main():
    st.title("Tool and Process Optimization Recommendations")

    tool = st.selectbox("Select Tool/Process", ["AWS S3", "AWS EC2", "AWS Lambda", "AWS Redshift", "AWS Aurora", "AWS Athena", "AWS EFS", "Apache Airflow", "Jenkins", "JIRA", "Bitbucket", "GitHub", "Snowflake", "Azure", "GCP"])

    if tool == "AWS S3":
        storage_size = st.number_input("Storage Size (GB)", min_value=0)
        duration = st.number_input("Storage Duration (days)", min_value=0)
        cost = st.number_input("Monthly Cost (USD)", min_value=0.0, format="%.2f")
        
        if st.button("Get Recommendations"):
            recommendations = get_aws_s3_recommendations(storage_size, duration, cost)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "AWS EC2":
        instance_type = st.text_input("Instance Type (e.g., t2.micro)")
        usage_hours = st.number_input("Monthly Usage Hours", min_value=0)
        cost = st.number_input("Monthly Cost (USD)", min_value=0.0, format="%.2f")
        
        if st.button("Get Recommendations"):
            recommendations = get_aws_ec2_recommendations(instance_type, usage_hours, cost)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "AWS Lambda":
        memory_size = st.number_input("Memory Size (MB)", min_value=0)
        duration = st.number_input("Average Duration (seconds)", min_value=0)
        invocations = st.number_input("Monthly Invocations", min_value=0)
        
        if st.button("Get Recommendations"):
            recommendations = get_aws_lambda_recommendations(memory_size, duration, invocations)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    # Add similar blocks for other AWS services...
    elif tool == "AWS Redshift":
        node_type = st.text_input("Node Type (e.g., dc2.large)")
        storage_size = st.number_input("Storage Size (GB)", min_value=0)
        query_count = st.number_input("Monthly Query Count", min_value=0)
    
        if st.button("Get Recommendations"):
            recommendations = get_aws_redshift_recommendations(node_type, storage_size, query_count)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "AWS Aurora":
        instance_class = st.text_input("Instance Class (e.g., db.r5.large)")
        storage_size = st.number_input("Storage Size (GB)", min_value=0)
        iops = st.number_input("IOPS", min_value=0)
    
        if st.button("Get Recommendations"):
            recommendations = get_aws_aurora_recommendations(instance_class, storage_size, iops)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "AWS Athena":
        query_count = st.number_input("Monthly Query Count", min_value=0)
        data_scanned = st.number_input("Data Scanned (GB)", min_value=0)
        cost = st.number_input("Monthly Cost (USD)", min_value=0.0, format="%.2f")
    
        if st.button("Get Recommendations"):
            recommendations = get_aws_athena_recommendations(query_count, data_scanned, cost)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "AWS EFS":
        storage_size = st.number_input("Storage Size (GB)", min_value=0)
        access_frequency = st.number_input("Access Frequency (times per month)", min_value=0)
        throughput_mode = st.selectbox("Throughput Mode", ["bursting", "provisioned"])
    
        if st.button("Get Recommendations"):
            recommendations = get_aws_efs_recommendations(storage_size, access_frequency, throughput_mode)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "Apache Airflow":
        concurrency = st.number_input("Concurrency", min_value=0)
        dag_count = st.number_input("Number of DAGs", min_value=0)
        task_duration = st.number_input("Task Duration (seconds)", min_value=0)
        
        if st.button("Get Recommendations"):
            recommendations = get_apache_airflow_recommendations(concurrency, dag_count, task_duration)
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "Jenkins":
        job_count = st.number_input("Number of Jobs", min_value=0)
        build_frequency = st.number_input("Build Frequency (per day)", min_value=0)
        
        recommendations = []
        if job_count > 100:  # Example threshold
            recommendations.append("Consider using folders and views to organize jobs.")
        if build_frequency > 50:  # Example threshold
            recommendations.append("Optimize build triggers and schedules to avoid unnecessary builds.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "JIRA":
        project_count = st.number_input("Number of Projects", min_value=0)
        user_count = st.number_input("Number of Users", min_value=0)
        
        recommendations = []
        if project_count > 50:  # Example threshold
            recommendations.append("Consider archiving old projects to improve performance.")
        if user_count > 100:  # Example threshold
            recommendations.append("Review user permissions and roles for better management.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "Bitbucket":
        repo_count = st.number_input("Number of Repositories", min_value=0)
        user_count = st.number_input("Number of Users", min_value=0)
        
        recommendations = []
        if repo_count > 100:  # Example threshold
            recommendations.append("Organize repositories using projects for better management.")
        if user_count > 50:  # Example threshold
            recommendations.append("Use branch permissions to control access and improve security.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "GitHub":
        repo_count = st.number_input("Number of Repositories", min_value=0)
        contributor_count = st.number_input("Number of Contributors", min_value=0)
        
        recommendations = []
        if repo_count > 50:  # Example threshold
            recommendations.append("Use GitHub Actions for automated workflows.")
        if contributor_count > 20:  # Example threshold
            recommendations.append("Implement code review processes to maintain code quality.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "Snowflake":
        warehouse_size = st.number_input("Warehouse Size", min_value=0)
        query_count = st.number_input("Number of Queries per Day", min_value=0)
        
        recommendations = []
        if warehouse_size > 10:  # Example threshold
            recommendations.append("Consider auto-scaling to manage costs and performance.")
        if query_count > 1000:  # Example threshold
            recommendations.append("Optimize query design and use caching for frequently run queries.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "Azure":
        vm_count = st.number_input("Number of VMs", min_value=0)
        storage_cost = st.number_input("Monthly Storage Cost (USD)", min_value=0.0, format="%.2f")
        
        recommendations = []
        if vm_count > 50:  # Example threshold
            recommendations.append("Consider using reserved instances for cost savings.")
        if storage_cost > 500:  # Example threshold
            recommendations.append("Review storage access patterns and optimize storage tiers.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

    elif tool == "GCP":
        instance_count = st.number_input("Number of Instances", min_value=0)
        monthly_cost = st.number_input("Monthly Cost (USD)", min_value=0.0, format="%.2f")
        
        recommendations = []
        if instance_count > 30:  # Example threshold
            recommendations.append("Use preemptible VMs for cost-effective batch processing.")
        if monthly_cost > 1000:  # Example threshold
            recommendations.append("Review your resource usage and consider committed use contracts.")
        
        if st.button("Get Recommendations"):
            st.write("Recommendations:")
            for rec in recommendations:
                st.write(f"- {rec}")

if __name__ == "__main__":
    main()
