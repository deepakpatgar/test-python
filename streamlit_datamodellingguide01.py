import streamlit as st

# Function to display a section with a title and content
def display_section(title, content):
    st.subheader(title)
    for item in content:
        st.write(f"- {item}")

# Data Modeling Best Practices App
st.title("Data Modeling Best Practices")

# Nomenclature and Naming Conventions
naming_conventions = [
    "Use clear, descriptive names for tables, columns, and keys.",
    "Avoid abbreviations unless they are widely understood.",
    "Use consistent case (e.g., snake_case or camelCase) throughout the model.",
    "Prefix primary keys with 'pk_' and foreign keys with 'fk_'.",
    "Tables should be named in singular form (e.g., 'Customer' instead of 'Customers').",
    "Columns representing dates should end with '_date' (e.g., 'created_date').",
    "Avoid using reserved SQL keywords as names for tables or columns.",
    "Maintain a glossary of abbreviations and naming conventions for consistency.",
    "Use prefixes or suffixes to indicate the role of a column (e.g., 'is_active' for a boolean flag).",
    "For tables representing events, use the '_event' suffix (e.g., 'purchase_event').",
    "Columns storing monetary values should end with '_amount' or '_value'.",
    "Define naming conventions for indexes, triggers, and constraints.",
    "Use singular nouns for entities and plural nouns for relationships.",
    "Establish and enforce naming standards across development teams.",
    "In multi-language environments, decide on a primary language for names."
]

display_section("Nomenclature and Naming Conventions", naming_conventions)

# Key Relationships
key_relationships = [
    "Ensure every table has a primary key.",
    "Use foreign keys to enforce relationships between tables.",
    "Normalize data to reduce redundancy, but denormalize for performance if necessary.",
    "Avoid composite primary keys if possible; use surrogate keys instead.",
    "Establish clear one-to-many, many-to-many, or one-to-one relationships.",
    "Ensure foreign keys reference primary keys in related tables.",
    "Use cascading updates and deletes only when necessary to maintain data integrity.",
    "Document all relationships in an ERD (Entity-Relationship Diagram).",
    "Use junction tables for many-to-many relationships.",
    "Avoid circular references between tables.",
    "Enforce referential integrity by using database constraints.",
    "Consider using natural keys in addition to surrogate keys where appropriate.",
    "Review and optimize join paths to avoid performance bottlenecks.",
    "Regularly review relationships to ensure they reflect current business logic.",
    "Apply appropriate indexing on foreign keys to improve join performance."
]

display_section("Key Relationships", key_relationships)

# Database, Table, and Column Best Practices
db_table_column_best_practices = [
    "Design tables with future growth in mind (e.g., consider partitioning large tables).",
    "Use appropriate data types for each column to optimize storage and performance.",
    "Index columns that are frequently used in WHERE clauses or JOIN conditions.",
    "Avoid using NULLs in columns that are part of a primary key or unique constraint.",
    "Document each table and column with descriptions and usage notes.",
    "Use unique constraints to enforce business rules.",
    "Regularly archive and purge old data to maintain database performance.",
    "Use check constraints to enforce data integrity at the column level.",
    "Avoid wide tables with too many columns; consider normalization.",
    "Use default values for columns where applicable to ensure data consistency.",
    "Implement triggers to enforce complex business rules where necessary.",
    "Use partitioning strategies to manage large datasets effectively.",
    "Regularly review and optimize index usage to maintain performance.",
    "Ensure that each table serves a clear and distinct purpose in the data model.",
    "Consider using views to simplify complex queries and present data more clearly."
]

display_section("Database, Table, and Column Best Practices", db_table_column_best_practices)

# Performance Tuning
performance_tuning = [
    "Optimize queries by using indexes and avoiding full table scans.",
    "Partition large tables to improve query performance.",
    "Use materialized views for complex or frequently accessed queries.",
    "Regularly analyze and optimize database statistics.",
    "Monitor query performance and adjust indexing strategies as needed.",
    "Avoid using SELECT * in queries; specify only the columns you need.",
    "Use query hints and execution plans to fine-tune query performance.",
    "Consider denormalization for read-heavy workloads to improve performance.",
    "Minimize the use of correlated subqueries; use joins instead.",
    "Batch data modifications to reduce the overhead of frequent small transactions.",
    "Use appropriate transaction isolation levels to balance performance and consistency.",
    "Regularly review and update statistics on tables and indexes.",
    "Use caching mechanisms to reduce load on the database for frequently accessed data.",
    "Optimize JOIN operations by ensuring indexes are used effectively.",
    "Monitor and optimize database memory usage and I/O operations."
]

display_section("Performance Tuning", performance_tuning)

# Administration and Optimization
admin_optimization = [
    "Implement regular backup and recovery strategies.",
    "Monitor database performance using tools like CloudWatch, Datadog, or native database tools.",
    "Optimize storage by archiving or purging old data.",
    "Ensure proper user access controls and data security policies are in place.",
    "Automate routine maintenance tasks (e.g., index rebuilding, vacuuming) where possible.",
    "Regularly audit and update user roles and permissions.",
    "Implement encryption at rest and in transit for sensitive data.",
    "Use automated alerts to monitor for unusual activity or performance issues.",
    "Regularly test disaster recovery plans to ensure they are effective.",
    "Implement replication and failover strategies for high availability.",
    "Optimize database configuration settings based on workload requirements.",
    "Use cloud-native tools for scaling and load balancing database resources.",
    "Regularly review and optimize storage usage, considering compression and deduplication.",
    "Implement data retention policies to manage storage costs and compliance.",
    "Document and automate database deployment and migration processes."
]

display_section("Administration and Optimization", admin_optimization)

# Guardrails and Important Tips
guardrails_tips = [
    "Enforce naming conventions through database policies or code reviews.",
    "Regularly review and update the data model to adapt to changing business requirements.",
    "Use a version control system to manage changes to the data model.",
    "Test the data model thoroughly before deploying to production.",
    "Establish clear governance processes for data modeling and database changes.",
    "Conduct regular data quality checks to ensure the accuracy and consistency of data.",
    "Use database migrations tools to track and apply schema changes in a controlled manner.",
    "Implement data masking and anonymization for sensitive data in non-production environments.",
    "Ensure that all changes to the data model are documented and reviewed by relevant stakeholders.",
    "Use role-based access control to limit who can make changes to the data model.",
    "Incorporate data lineage tracking to understand the flow and transformation of data.",
    "Implement data validation rules at the database level to enforce business logic.",
    "Use database triggers carefully, as they can impact performance and complicate debugging.",
    "Regularly review and optimize database indexes to ensure they are aligned with query patterns.",
    "Consider the impact of changes to the data model on existing reports, dashboards, and applications."
]

display_section("Guardrails and Important Tips", guardrails_tips)

# Footer
st.write("This application provides a summary of best practices and guidelines for data modeling. "
         "Always consider specific use cases and business requirements when applying these practices.")

