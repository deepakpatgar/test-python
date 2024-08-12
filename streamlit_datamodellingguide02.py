import streamlit as st

# Function to display a section with a title and content
def display_section(title, content):
    st.subheader(title)
    for item in content:
        st.write(f"- {item['point']}")
        if 'example' in item:
            st.code(item['example'], language='sql')

# Data Modeling Best Practices App
st.title("Data Modeling Best Practices")

# Nomenclature and Naming Conventions
naming_conventions = [
    {"point": "Use clear, descriptive names for tables, columns, and keys.",
     "example": "Table: `Customer`, Column: `first_name`"},
    {"point": "Avoid abbreviations unless they are widely understood.",
     "example": "Use `Address` instead of `Addr`, `Quantity` instead of `Qty`."},
    {"point": "Use consistent case (e.g., snake_case or camelCase) throughout the model.",
     "example": "snake_case: `order_date`, camelCase: `orderDate`"},
    {"point": "Prefix primary keys with 'pk_' and foreign keys with 'fk_'.",
     "example": "Primary Key: `pk_customer_id`, Foreign Key: `fk_order_customer_id`"},
    {"point": "Tables should be named in singular form (e.g., 'Customer' instead of 'Customers')."},
    {"point": "Columns representing dates should end with '_date'.",
     "example": "Column: `created_date`, `updated_date`"},
    {"point": "Avoid using reserved SQL keywords as names for tables or columns.",
     "example": "Avoid using `select`, `table`, `order` as table or column names."},
    {"point": "Maintain a glossary of abbreviations and naming conventions for consistency."},
    {"point": "Use prefixes or suffixes to indicate the role of a column.",
     "example": "Column: `is_active` (boolean flag), `total_amount` (numeric)"},
    {"point": "For tables representing events, use the '_event' suffix.",
     "example": "Table: `login_event`, `purchase_event`"},
    {"point": "Columns storing monetary values should end with '_amount' or '_value'.",
     "example": "Column: `total_amount`, `discount_value`"},
    {"point": "Define naming conventions for indexes, triggers, and constraints.",
     "example": "Index: `idx_customer_last_name`, Constraint: `chk_order_status`"},
    {"point": "Use singular nouns for entities and plural nouns for relationships.",
     "example": "Entity: `Customer`, Relationship: `Customer_Orders`"},
    {"point": "Establish and enforce naming standards across development teams."},
    {"point": "In multi-language environments, decide on a primary language for names."}
]

display_section("Nomenclature and Naming Conventions", naming_conventions)

# Key Relationships
key_relationships = [
    {"point": "Ensure every table has a primary key.",
     "example": "CREATE TABLE Customer (pk_customer_id SERIAL PRIMARY KEY, ...);"},
    {"point": "Use foreign keys to enforce relationships between tables.",
     "example": "CREATE TABLE Order (pk_order_id SERIAL PRIMARY KEY, fk_customer_id INT REFERENCES Customer(pk_customer_id));"},
    {"point": "Normalize data to reduce redundancy, but denormalize for performance if necessary."},
    {"point": "Avoid composite primary keys if possible; use surrogate keys instead.",
     "example": "Use `pk_order_id` as a surrogate key instead of `order_number, order_date` as a composite key."},
    {"point": "Establish clear one-to-many, many-to-many, or one-to-one relationships.",
     "example": "One-to-Many: A customer can place many orders."},
    {"point": "Ensure foreign keys reference primary keys in related tables.",
     "example": "Foreign Key: `fk_customer_id INT REFERENCES Customer(pk_customer_id)`"},
    {"point": "Use cascading updates and deletes only when necessary to maintain data integrity.",
     "example": "ON DELETE CASCADE or ON UPDATE CASCADE in foreign key definitions."},
    {"point": "Document all relationships in an ERD (Entity-Relationship Diagram)."},
    {"point": "Use junction tables for many-to-many relationships.",
     "example": "CREATE TABLE Enrollment (fk_student_id INT, fk_course_id INT, PRIMARY KEY (fk_student_id, fk_course_id));"},
    {"point": "Avoid circular references between tables."},
    {"point": "Enforce referential integrity by using database constraints.",
     "example": "FOREIGN KEY (fk_customer_id) REFERENCES Customer(pk_customer_id) ON DELETE RESTRICT"},
    {"point": "Consider using natural keys in addition to surrogate keys where appropriate.",
     "example": "Natural Key: `email` in a `User` table, Surrogate Key: `pk_user_id`."},
    {"point": "Review and optimize join paths to avoid performance bottlenecks."},
    {"point": "Regularly review relationships to ensure they reflect current business logic."},
    {"point": "Apply appropriate indexing on foreign keys to improve join performance."}
]

display_section("Key Relationships", key_relationships)

# Database, Table, and Column Best Practices
db_table_column_best_practices = [
    {"point": "Design tables with future growth in mind (e.g., consider partitioning large tables)."},
    {"point": "Use appropriate data types for each column to optimize storage and performance.",
     "example": "Use `VARCHAR(255)` for text fields, `INT` for integers, `DATE` for dates."},
    {"point": "Index columns that are frequently used in WHERE clauses or JOIN conditions.",
     "example": "CREATE INDEX idx_order_date ON Order(order_date);"},
    {"point": "Avoid using NULLs in columns that are part of a primary key or unique constraint.",
     "example": "Ensure `pk_customer_id` and `email` in a `Customer` table are NOT NULL."},
    {"point": "Document each table and column with descriptions and usage notes.",
     "example": "COMMENT ON COLUMN Customer.email IS 'Customer email address, used for login';"},
    {"point": "Use unique constraints to enforce business rules.",
     "example": "CREATE UNIQUE INDEX idx_customer_email ON Customer(email);"},
    {"point": "Regularly archive and purge old data to maintain database performance."},
    {"point": "Use check constraints to enforce data integrity at the column level.",
     "example": "CHECK (order_status IN ('pending', 'shipped', 'delivered'))"},
    {"point": "Avoid wide tables with too many columns; consider normalization."},
    {"point": "Use default values for columns where applicable to ensure data consistency.",
     "example": "CREATE TABLE Product (product_id SERIAL PRIMARY KEY, in_stock BOOLEAN DEFAULT TRUE);"},
    {"point": "Implement triggers to enforce complex business rules where necessary.",
     "example": "CREATE TRIGGER update_timestamp BEFORE UPDATE ON Order FOR EACH ROW EXECUTE FUNCTION update_modified_date();"},
    {"point": "Use partitioning strategies to manage large datasets effectively.",
     "example": "Partitioning a table by `year` to optimize queries for recent data."},
    {"point": "Regularly review and optimize index usage to maintain performance."},
    {"point": "Ensure that each table serves a clear and distinct purpose in the data model."},
    {"point": "Consider using views to simplify complex queries and present data more clearly.",
     "example": "CREATE VIEW CustomerOrders AS SELECT Customer.name, Order.order_date FROM Customer JOIN Order ON Customer.pk_customer_id = Order.fk_customer_id;"}
]

display_section("Database, Table, and Column Best Practices", db_table_column_best_practices)

# Performance Tuning
performance_tuning = [
    {"point": "Optimize queries by using indexes and avoiding full table scans.",
     "example": "Use `EXPLAIN` to analyze query performance and ensure indexes are being used."},
    {"point": "Partition large tables to improve query performance.",
     "example": "CREATE TABLE Sales PARTITION BY RANGE (sale_date) (PARTITION p1 VALUES LESS THAN ('2023-01-01'), PARTITION p2 VALUES LESS THAN ('2024-01-01'));"},
    {"point": "Use materialized views for complex or frequently accessed queries.",
     "example": "CREATE MATERIALIZED VIEW RecentOrders AS SELECT * FROM Order WHERE order_date > CURRENT_DATE - INTERVAL '30 days';"},
    {"point": "Regularly analyze and optimize database statistics.",
     "example": "Use `ANALYZE` to update statistics for query optimization."},
    {"point": "Monitor query performance and adjust indexing strategies as needed."},
    {"point": "Avoid using SELECT * in queries; specify only the columns you need.",
     "example": "SELECT first_name, last_name FROM Customer WHERE customer_id = 123;"},
    {"point": "Use query hints and execution plans to fine-tune query performance.",
     "example": "SELECT /*+ INDEX(Order idx_order_date) */ order_id, customer_id FROM Order WHERE order_date = '2024-08-01';"},
    {"point": "Consider denormalization for read-heavy workloads to improve performance."},
    {"point": "Minimize the use of correlated subqueries; use joins instead.",
     "example": "Use `JOIN` instead of `WHERE EXISTS (SELECT ...)`."},
    {"point": "Batch data modifications to reduce the overhead of frequent small transactions."},
    {"point": "Use appropriate transaction isolation levels to balance performance and consistency.",
     "example": "Set isolation level to `READ COMMITTED` for transactions where dirty reads are acceptable."},
    {"point": "Regularly review and update statistics on tables and indexes."},
    {"point": "Use caching mechanisms to reduce load on the database for frequently accessed data.",
     "example": "Consider using Redis or Memcached for caching."},
    {"point": "Optimize JOIN operations by ensuring indexes are used effectively."},
    {"point": "Monitor and optimize database memory usage and I/O operations."}
]

display_section("Performance Tuning", performance_tuning)

# Administration and Optimization
admin_optimization = [
    {"point": "Implement regular backup and recovery strategies."},
    {"point": "Monitor database performance using tools like CloudWatch, Datadog, or native database tools."},
    {"point": "Optimize storage by archiving or purging old data.",
     "example": "Consider using AWS Glacier for long-term storage of archived data."},
    {"point": "Ensure proper user access controls and data security policies are in place.",
     "example": "Use `GRANT` and `REVOKE` to manage user permissions."},
    {"point": "Automate routine maintenance tasks (e.g., index rebuilding, vacuuming) where possible."},
    {"point": "Regularly audit and update user roles and permissions.",
     "example": "Review roles using `SELECT * FROM pg_roles;`."},
    {"point": "Implement encryption at rest and in transit for sensitive data.",
     "example": "Use `pgcrypto` for encrypting data in PostgreSQL."},
    {"point": "Use automated alerts to monitor for unusual activity or performance issues.",
     "example": "Set up alerts for slow queries or high CPU usage."},
    {"point": "Regularly test disaster recovery plans to ensure they are effective."},
    {"point": "Implement replication and failover strategies for high availability.",
     "example": "Use PostgreSQL streaming replication or AWS RDS multi-AZ for failover."},
    {"point": "Optimize database configuration settings based on workload requirements.",
     "example": "Adjust `work_mem` and `shared_buffers` settings for optimal performance."},
    {"point": "Use cloud-native tools for scaling and load balancing database resources.",
     "example": "Leverage AWS Aurora Auto Scaling for dynamic scaling of database resources."},
    {"point": "Regularly review and optimize storage usage, considering compression and deduplication.",
     "example": "Use `pg_compress` or similar tools for compressing large datasets."},
    {"point": "Implement data retention policies to manage storage costs and compliance.",
     "example": "Automate data purging using scheduled jobs or triggers."},
    {"point": "Document and automate database deployment and migration processes.",
     "example": "Use tools like Flyway or Liquibase for managing database migrations."}
]

display_section("Administration and Optimization", admin_optimization)

# Guardrails and Important Tips
guardrails_tips = [
    {"point": "Enforce naming conventions through database policies or code reviews."},
    {"point": "Regularly review and update the data model to adapt to changing business requirements."},
    {"point": "Use a version control system to manage changes to the data model.",
     "example": "Use Git for version control of database scripts and migrations."},
    {"point": "Test the data model thoroughly before deploying to production."},
    {"point": "Establish clear governance processes for data modeling and database changes."},
    {"point": "Conduct regular data quality checks to ensure the accuracy and consistency of data.",
     "example": "Use tools like dbt or Dataform for automated data testing and quality checks."},
    {"point": "Use database migrations tools to track and apply schema changes in a controlled manner.",
     "example": "Tools like Liquibase or Flyway help manage schema changes with version control."},
    {"point": "Implement data masking and anonymization for sensitive data in non-production environments.",
     "example": "Use tools like `pgcrypto` or database-level masking features for anonymization."},
    {"point": "Ensure that all changes to the data model are documented and reviewed by relevant stakeholders."},
    {"point": "Use role-based access control to limit who can make changes to the data model.",
     "example": "GRANT ALTER ON SCHEMA public TO db_admin_role;"},
    {"point": "Incorporate data lineage tracking to understand the flow and transformation of data.",
     "example": "Use tools like Apache Atlas or AWS Glue Data Catalog for lineage tracking."},
    {"point": "Implement data validation rules at the database level to enforce business logic.",
     "example": "Use `CHECK` constraints or triggers for enforcing complex rules."},
    {"point": "Use database triggers carefully, as they can impact performance and complicate debugging.",
     "example": "Avoid complex logic in triggers to reduce performance overhead."},
    {"point": "Regularly review and optimize database indexes to ensure they are aligned with query patterns."},
    {"point": "Consider the impact of changes to the data model on existing reports, dashboards, and applications."}
]

display_section("Guardrails and Important Tips", guardrails_tips)

# Footer
st.write("This application provides a summary of best practices and guidelines for data modeling. "
         "Always consider specific use cases and business requirements when applying these practices.")
