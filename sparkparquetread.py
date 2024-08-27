import pyarrow.parquet as pq

# Path to the Parquet file
parquet_file_path = 'sample_customers.parquet'

# Read the Parquet file
table = pq.read_table(parquet_file_path)

# Convert to a Pandas DataFrame
df = table.to_pandas()

# Display the DataFrame
print(df)

# Path to the Parquet file
parquet_file_path = 'sample_customers.parquet'

# Read the Parquet file
parquet_file = pq.ParquetFile(parquet_file_path)

# Print the schema
print(parquet_file.schema)

# Access metadata
metadata = parquet_file.metadata

# Print metadata
print(metadata)
