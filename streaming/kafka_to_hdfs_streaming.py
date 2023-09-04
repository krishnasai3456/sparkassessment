from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType
import json

# Load config
with open("config/streaming_config.json", "r") as config_file:
    streaming_config = json.load(config_file)

# Get Spark session
spark = SparkSession.builder \
    .appName("KafkaToHDFSSparkStreaming") \
    .getOrCreate()

#  Kafka source
kafka_source = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", streaming_config["kafka"]["bootstrap.servers"]) \
    .option("subscribe", streaming_config["kafka"]["topic"]) \
    .load()

xml_schema = StructType()
schema = batch_config["schema"]["filepath"]

parsed_data = kafka_source.selectExpr("CAST(value AS STRING) as xml_data") \
    .selectExpr("from_xml(xml_data, schema) as data") \
    .select("data.*")
# perform validation
temp_df = validate_and_format_wrapper(parsed_data,,schema)
#write back to processed zone
query = temp_df.writeStream \
    .format("parquet") \
    .option("path", streaming_config["hdfs"]["parquet_output_path"]) \
    .outputMode("append") \
    .trigger(processingTime=streaming_config["trigger_interval"]) \
    .start()

query.awaitTermination()

spark.stop()