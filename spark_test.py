from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("HelloSpark").getOrCreate()

# Make a simple DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

print("✅ Spark DataFrame created:")
df.show()

# Stop Spark
spark.stop()
