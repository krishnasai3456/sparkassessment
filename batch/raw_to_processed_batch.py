from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import json

from  utils.xml_parser import parse_and_flatten_xml_wrapper

# config load
with open("config/batch_config.json", "r") as config_file:
    batch_config = json.load(config_file)

# Get spark session
spark = SparkSession.builder \
    .appName("RawToProcessedBatch") \
    .getOrCreate()

# Read raw data from HDFS
raw_data = spark.read.parquet(batch_config["hdfs"]["raw_input_path"])

# Read config
raw_input_path = batch_config["hdfs"]["raw_input_path"]
processed_output_path = batch_config["hdfs"]["raw_input_path"]
schema = batch_config["schema"]["filepath"]

#parse and flatten XML to DF
raw_input_df = parse_and_flatten_xml_wrapper(raw_input_path)

# Perform VAlidaiton
temp_df = validate_and_format_wrapper(raw_input_df,schema)

# add date column
processed_data = temp_df \
    .withColumn("date_partition", col("date_field").cast("date"))

# write back to processed output path
processed_data.write \
    .partitionBy("date_partition") \
    .parquet(batch_config["hdfs"]["processed_output_path"], mode="overwrite")

