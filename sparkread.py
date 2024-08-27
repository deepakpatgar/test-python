from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ParquetExample").getOrCreate()

# Path to the Parquet file
parquet_file_path = 'sample_customers.parquet'

# Read the Parquet file
df = spark.read.parquet(parquet_file_path)

# Show the DataFrame
df.show()
