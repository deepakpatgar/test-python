import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Sample data
data = {
    'customer_id': [101, 102, 103],
    'name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'email': ['john@example.com', 'jane@example.com', 'alice@example.com'],
    'signup_date': ['2023-01-15', '2023-01-20', '2023-02-10'],
    'total_purchases': [3000.00, 1500.00, 500.00]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the DataFrame to a Parquet file
parquet_file_path = 'sample_customers.parquet'
df.to_parquet(parquet_file_path, index=False)

print(f'Sample Parquet file created: {parquet_file_path}')
