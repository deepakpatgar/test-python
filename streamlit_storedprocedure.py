import streamlit as st

# Define sections for each database with additional points and examples
def snowflake_section():
    st.header("Snowflake Stored Procedures and Functions")
    st.subheader("Guide")
    st.write("Snowflake supports stored procedures and functions written in JavaScript. Procedures encapsulate complex logic and execute on Snowflake.")

    st.subheader("Best Practices")
    st.write(
        """
        - **Use JavaScript for Procedures**: Write procedures in JavaScript to leverage Snowflake's execution engine.
        - **Optimize Performance**: Limit the data processed in procedures to reduce execution time. Use Snowflake's `RESULT_SCAN` to work with results from queries.
        - **Error Handling**: Implement try-catch blocks for managing errors gracefully.
        - **Version Control**: Maintain versions of your procedures for better tracking and rollback capabilities.
        - **Testing**: Thoroughly test procedures with various data inputs to ensure reliability.
        - **Avoid Large Transactions**: Break down large transactions to prevent hitting Snowflake's limits.
        - **Use Secure UDFs**: If using User-Defined Functions (UDFs), ensure they are secure and perform necessary validations.
        - **Utilize Streams**: Use Snowflake Streams to capture changes to data tables if your procedures depend on real-time data.
        - **Document Procedures**: Maintain clear documentation within your procedures for better maintainability.
        - **Schedule Procedures**: Use Snowflake Tasks to automate the execution of stored procedures at scheduled intervals.
        """
    )
    
    st.subheader("Guardrails")
    st.write(
        """
        - **Limit Permissions**: Grant execute permissions only to necessary roles.
        - **Monitor Performance**: Utilize Snowflake's QUERY_HISTORY and INFORMATION_SCHEMA to track performance.
        - **Logging**: Implement logging within procedures to track execution flow and issues.
        - **Avoid Long-Running Procedures**: Break down long-running procedures into smaller, manageable parts.
        - **Resource Management**: Monitor and manage Snowflake credits to optimize cost.
        - **Concurrency Control**: Manage concurrent procedure executions to prevent contention issues.
        - **Review Query Plans**: Regularly review and optimize query execution plans.
        - **Use Transactions Wisely**: Handle transactions efficiently to avoid locking issues.
        - **Set Limits on Data Processed**: Establish limits on the amount of data processed by procedures to prevent performance degradation.
        - **Regular Audits**: Perform regular audits of stored procedures for security and performance.
        """
    )
    
    st.subheader("Important Tips")
    st.write(
        """
        - **Use `PROCEDURE` Keyword**: Define procedures using the `PROCEDURE` keyword.
        - **Debugging**: Use Snowflake’s debugging features to troubleshoot issues in your procedures.
        - **Consider Using Task Chains**: For complex workflows, use Snowflake Tasks in combination to manage dependencies.
        - **Handle Exceptions Carefully**: Ensure all potential exceptions are handled to avoid unexpected failures.
        - **Review Documentation**: Regularly update and review documentation for accuracy.
        - **Test in Isolated Environments**: Conduct tests in isolated environments to avoid impacting production data.
        - **Employ Data Validation**: Implement data validation within procedures to ensure data integrity.
        - **Optimize Data Loading**: Use optimized methods for loading data into tables when using procedures.
        - **Consider Alternative Approaches**: Evaluate if stored procedures are the best solution or if alternative Snowflake features could be used.
        - **Engage with Snowflake Support**: For complex issues, don’t hesitate to reach out to Snowflake support for assistance.
        """
    )
    
    st.subheader("Examples")
    st.code(
        """
        -- Example of a Snowflake procedure
        CREATE OR REPLACE PROCEDURE example_procedure (input_param STRING)
        RETURNS STRING
        LANGUAGE JAVASCRIPT
        EXECUTE AS CALLER
        AS
        $$
        var result;
        try {
            var sql_command = "SELECT COUNT(*) FROM my_table WHERE column = '" + input_param + "'";
            var stmt = snowflake.createStatement({sqlText: sql_command});
            var rs = stmt.execute();
            result = rs.getColumnValue(1);
        } catch(err) {
            result = "Error: " + err.message;
        }
        return result;
        $$
        ;
        """
    )

def oracle_section():
    st.header("Oracle Stored Procedures and Functions")
    st.subheader("Guide")
    st.write("Oracle uses PL/SQL for stored procedures and functions. PL/SQL offers advanced control structures and exception handling.")

    st.subheader("Best Practices")
    st.write(
        """
        - **Use PL/SQL Blocks**: Structure code into PL/SQL blocks for clarity and manageability.
        - **Exception Handling**: Use `EXCEPTION` blocks to handle errors and exceptions.
        - **Optimize Queries**: Ensure that queries within procedures are well-optimized to enhance performance.
        - **Modular Design**: Break complex procedures into smaller, reusable procedures.
        - **Documentation**: Document procedures with comments to improve maintainability.
        - **Use Bind Variables**: Use bind variables to improve performance and prevent SQL injection.
        - **Minimize Hard-Coding**: Avoid hard-coding values and use parameters or configuration tables instead.
        - **Avoid Cursors Where Possible**: Use set-based operations instead of cursors to enhance performance.
        - **Regularly Review Execution Plans**: Periodically review execution plans for optimization opportunities.
        - **Manage Dependencies**: Handle dependencies carefully to avoid issues during procedure execution.
        """
    )
    
    st.subheader("Guardrails")
    st.write(
        """
        - **Access Control**: Limit access to stored procedures to authorized users.
        - **Performance Monitoring**: Use Oracle's performance tools like AWR reports for monitoring.
        - **Version Control**: Track changes to procedures with version control systems.
        - **Testing**: Perform thorough testing in a development environment before production deployment.
        - **Use Schema Privileges**: Grant only necessary schema privileges to minimize security risks.
        - **Regular Audits**: Conduct regular audits of stored procedures for security and performance.
        - **Avoid Long Transactions**: Keep transactions short to prevent locking issues.
        - **Backup Procedures**: Ensure procedures are backed up regularly.
        - **Review and Refactor**: Regularly review and refactor procedures for optimization.
        - **Security Checks**: Perform regular security checks to protect against vulnerabilities.
        """
    )
    
    st.subheader("Important Tips")
    st.write(
        """
        - **Use `CREATE OR REPLACE`**: Use `CREATE OR REPLACE` to update procedures.
        - **PL/SQL Debugging**: Utilize Oracle SQL Developer for debugging and profiling.
        - **Implement Logging**: Include logging in procedures for troubleshooting.
        - **Avoid Nested Transactions**: Keep transactions simple and avoid nesting.
        - **Monitor Resource Usage**: Keep an eye on resource usage to prevent issues.
        - **Consider Performance Impacts**: Evaluate the performance impacts of procedures on the database.
        - **Utilize Profiling Tools**: Use Oracle profiling tools to understand performance bottlenecks.
        - **Update Documentation**: Keep documentation up-to-date with changes to procedures.
        - **Consider Partitioning**: Use partitioning for large tables to improve performance.
        - **Consult Documentation**: Refer to Oracle's documentation for advanced features and capabilities.
        """
    )
    
    st.subheader("Examples")
    st.code(
        """
        -- Example of an Oracle PL/SQL procedure
        CREATE OR REPLACE PROCEDURE example_procedure (input_param IN VARCHAR2, output_param OUT NUMBER)
        IS
        BEGIN
            SELECT COUNT(*) INTO output_param FROM my_table WHERE column = input_param;
        EXCEPTION
            WHEN OTHERS THEN
                output_param := -1;
                DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        END;
        """
    )

def mssql_section():
    st.header("MS SQL Server Stored Procedures and Functions")
    st.subheader("Guide")
    st.write("MS SQL Server uses Transact-SQL (T-SQL) for creating stored procedures and functions, extending SQL with procedural programming features.")

    st.subheader("Best Practices")
    st.write(
        """
        - **Use Transactions**: Wrap procedures in transactions to maintain data integrity.
        - **Error Handling**: Use `TRY...CATCH` blocks for handling errors.
        - **Parameterize Queries**: Use parameters to protect against SQL injection and improve performance.
        - **Optimize Execution Plans**: Regularly analyze execution plans for performance improvements.
        - **Avoid Cursors**: Prefer set-based operations over cursors for better performance.
        - **Implement Logging**: Include logging within procedures to trace execution and errors.
        - **Use Dynamic SQL Carefully**: Use dynamic SQL with caution and sanitize inputs to prevent SQL injection.
        - **Maintain Indexes**: Ensure appropriate indexing to support query performance within procedures.
        - **Regularly Review Security**: Periodically review security settings for stored procedures.
        - **Consider Stored Procedure Complexity**: Simplify complex stored procedures to improve maintainability.
        """
    )
    
    st.subheader("Guardrails")
    st.write(
        """
        - **Limit Permissions**: Restrict procedure execution to necessary roles.
        - **Monitor Performance**: Use SQL Server’s tools like SQL Profiler and DMVs.
        - **Testing**: Ensure thorough testing in a non-production environment.
        - **Documentation**: Keep procedures well-documented for future maintenance.
        - **Audit Procedures**: Regularly audit procedures to ensure compliance and performance.
        - **Avoid Excessive Use of Temporary Tables**: Limit the use of temporary tables to avoid performance issues.
        - **Control Execution Time**: Set timeouts to prevent long-running procedures from impacting performance.
        - **Monitor Resource Utilization**: Keep track of resource utilization to avoid contention issues.
        - **Implement Code Reviews**: Conduct code reviews to ensure quality and security.
        - **Version Control**: Use version control for procedures to manage changes and rollbacks.
        """
    )
    
    st.subheader("Important Tips")
    st.write(
        """
        - **Use `EXEC` for Execution**: Execute procedures using the `EXEC` statement.
        - **Debugging**: Use SQL Server Management Studio (SSMS) for debugging stored procedures.
        - **Avoid Hard-Coding Values**: Use parameters instead of hard-coding values in procedures.
        - **Consider Procedure Caching**: Take advantage of SQL Server's procedure caching to improve performance.
        - **Keep Transactions Short**: Ensure transactions within procedures are kept as short as possible.
        - **Utilize SQL Server Profiler**: Use SQL Server Profiler to monitor procedure performance.
        - **Review Query Execution Plans**: Regularly review execution plans for optimization.
        - **Optimize Indexing**: Ensure that indexes support the queries executed within procedures.
        - **Update Statistics**: Keep statistics updated for tables used in procedures.
        - **Leverage Query Store**: Use Query Store to track performance and manage queries.
        """
    )
    
    st.subheader("Examples")
    st.code(
        """
        -- Example of a SQL Server stored procedure
        CREATE PROCEDURE example_procedure
            @input_param NVARCHAR(50),
            @output_param INT OUTPUT
        AS
        BEGIN
            SET NOCOUNT ON;
            BEGIN TRY
                SELECT @output_param = COUNT(*) FROM my_table WHERE column = @input_param;
            END TRY
            BEGIN CATCH
                SET @output_param = -1;
                PRINT 'Error: ' + ERROR_MESSAGE();
            END CATCH
        END;
        """
    )

def mysql_section():
    st.header("MySQL Stored Procedures and Functions")
    st.subheader("Guide")
    st.write("MySQL allows you to create stored procedures and functions using its own procedural language, offering flexibility for complex operations.")

    st.subheader("Best Practices")
    st.write(
        """
        - **Keep Procedures Simple**: Design procedures to perform specific tasks efficiently.
        - **Error Handling**: Use `DECLARE ... HANDLER` to manage exceptions.
        - **Optimize Performance**: Index tables and optimize queries to enhance performance.
        - **Document Procedures**: Provide thorough documentation for easier maintenance.
        - **Modular Approach**: Divide complex logic into smaller procedures where possible.
        - **Use Prepared Statements**: Utilize prepared statements to protect against SQL injection.
        - **Manage Temporary Tables**: Clean up temporary tables to avoid resource leakage.
        - **Limit Procedure Complexity**: Avoid overly complex procedures to maintain clarity and performance.
        - **Implement Security Measures**: Ensure procedures are secured against unauthorized access.
        - **Consider Performance Benchmarks**: Regularly benchmark performance to identify and address issues.
        """
    )
    
    st.subheader("Guardrails")
    st.write(
        """
        - **Restrict Access**: Control access to procedures using MySQL’s privilege system.
        - **Monitor Usage**: Use MySQL’s profiling tools to monitor performance.
        - **Version Management**: Manage versions of procedures using a version control system.
        - **Testing**: Perform rigorous testing in a development environment.
        - **Resource Management**: Monitor and manage resource usage to prevent issues.
        - **Avoid Long-Running Procedures**: Prevent long-running procedures from impacting server performance.
        - **Regular Reviews**: Conduct regular reviews of stored procedures for security and efficiency.
        - **Backup Procedures**: Ensure that stored procedures are included in regular backups.
        - **Manage Dependencies**: Handle dependencies carefully to avoid issues with procedure execution.
        - **Optimize Query Performance**: Regularly optimize queries within procedures for better performance.
        """
    )
    
    st.subheader("Important Tips")
    st.write(
        """
        - **Use `CALL` for Execution**: Execute procedures using the `CALL` statement.
        - **Debugging**: Utilize MySQL Workbench or similar tools for debugging.
        - **Employ Data Validation**: Implement data validation within procedures to ensure data integrity.
        - **Avoid Excessive Logging**: Balance logging to avoid performance degradation.
        - **Review Execution Plans**: Analyze execution plans to identify optimization opportunities.
        - **Keep Procedures Up-to-Date**: Regularly update procedures to align with changes in the database schema.
        - **Use Consistent Naming Conventions**: Adopt consistent naming conventions for ease of management.
        - **Consider Stored Function Use**: Use stored functions where appropriate for data calculations.
        - **Monitor Procedure Execution**: Keep track of procedure execution times and optimize as needed.
        - **Consult MySQL Documentation**: Refer to MySQL’s documentation for advanced features and best practices.
        """
    )
    
    st.subheader("Examples")
    st.code(
        """
        -- Example of a MySQL stored procedure
        DELIMITER $$
        CREATE PROCEDURE example_procedure(IN input_param VARCHAR(50), OUT output_param INT)
        BEGIN
            DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
            BEGIN
                SET output_param = -1;
            END;

            SELECT COUNT(*) INTO output_param FROM my_table WHERE column = input_param;
        END$$
        DELIMITER ;
        """
    )

def redshift_section():
    st.header("AWS Redshift Stored Procedures and Functions")
    st.subheader("Guide")
    st.write("AWS Redshift supports stored procedures written in PL/pgSQL, offering a way to handle complex transformations and logic.")

    st.subheader("Best Practices")
    st.write(
        """
        - **Use PL/pgSQL**: Write stored procedures in PL/pgSQL to leverage Redshift’s capabilities.
        - **Optimize Performance**: Minimize the amount of data processed within procedures and use appropriate data distribution keys.
        - **Error Handling**: Use `EXCEPTION` blocks to handle errors.
        - **Data Distribution**: Consider data distribution and sort keys to optimize query performance.
        - **Documentation**: Document procedures for better maintainability.
        - **Use Temporary Tables**: Utilize temporary tables for intermediate results, but clean them up promptly.
        - **Regularly Update Statistics**: Ensure statistics are up-to-date for better query optimization.
        - **Monitor Query Performance**: Regularly monitor the performance of queries within procedures.
        - **Utilize Redshift’s Query Monitoring**: Use Redshift’s query monitoring features to track and analyze procedure execution.
        - **Version Control**: Implement version control for procedures to manage changes and rollbacks.
        """
    )
    
    st.subheader("Guardrails")
    st.write(
        """
        - **Limit Procedure Permissions**: Restrict access to procedures based on user roles.
        - **Monitor Performance**: Utilize Redshift’s system tables and logs for performance monitoring.
        - **Testing**: Conduct thorough testing in a development environment before deploying to production.
        - **Version Control**: Track changes to procedures with version control.
        - **Resource Management**: Manage cluster resources to avoid performance bottlenecks.
        - **Avoid Excessive Logging**: Implement logging in a way that does not impact performance.
        - **Handle Large Data Volumes**: Manage large data volumes carefully to avoid performance degradation.
        - **Regular Audits**: Perform regular audits of procedures for security and performance.
        - **Manage Concurrency**: Handle concurrent procedure executions to avoid contention issues.
        - **Review Execution Plans**: Regularly review execution plans for optimization opportunities.
        """
    )
    
    st.subheader("Important Tips")
    st.write(
        """
        - **Use `CREATE PROCEDURE`**: Define procedures with the `CREATE PROCEDURE` statement.
        - **Debugging**: Leverage Redshift’s system tables for debugging and troubleshooting.
        - **Optimize Data Loading**: Use optimized methods for loading data into tables when using procedures.
        - **Regularly Review Performance**: Periodically review the performance of stored procedures.
        - **Use Query Store**: Utilize Query Store for tracking and managing query performance.
        - **Monitor Disk Space**: Keep track of disk space usage to avoid issues with large procedures.
        - **Ensure Data Consistency**: Verify data consistency before and after executing procedures.
        - **Consider Procedure Complexity**: Simplify complex procedures to improve maintainability and performance.
        - **Engage with AWS Support**: Seek assistance from AWS support for complex issues related to Redshift.
        - **Stay Updated**: Keep up-to-date with Redshift updates and best practices for continued optimization.
        """
    )
    
    st.subheader("Examples")
    st.code(
        """
        -- Example of an AWS Redshift stored procedure
        CREATE OR REPLACE PROCEDURE example_procedure (IN input_param VARCHAR)
        LANGUAGE plpgsql
        AS $$
        DECLARE
            output_param INT;
        BEGIN
            BEGIN
                SELECT COUNT(*) INTO output_param FROM my_table WHERE column = input_param;
            EXCEPTION
                WHEN OTHERS THEN
                    output_param := -1;
                    RAISE NOTICE 'Error: %', SQLERRM;
            END;
        END;
        $$;
        """
    )

# Streamlit App Layout
def main():
    st.title("Stored Procedures and Functions Guide")
    
    # Create tabs for each section
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Snowflake", "Oracle", "MS SQL Server", "MySQL", "AWS Redshift"])
    
    with tab1:
        snowflake_section()
    
    with tab2:
        oracle_section()
    
    with tab3:
        mssql_section()
    
    with tab4:
        mysql_section()
    
    with tab5:
        redshift_section()

if __name__ == "__main__":
    main()
