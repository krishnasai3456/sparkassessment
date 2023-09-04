#!/bin/bash

SPARK_HOME=/path/to/spark
SCRIPT_LOC=../scripts/submit_streaming_jobs.sh 
LOG_DIR=../logs/
APP_NAME="RawToProcessedBatch"
CHECKPOINT_DIR=../checkpoints/

$SPARK_HOME/bin/spark-submit \
  --name "$APP_NAME" \
  --master yarn \
  --deploy-mode cluster \
  --class com.example.StreamingAppMain  
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0
  --conf spark.streaming.stopGracefullyOnShutdown=true \
  --conf spark.driver.extraJavaOptions=-Dlog4j.configuration=file:/path/to/log4j.properties \
  --conf spark.executor.extraJavaOptions=-Dlog4j.configuration=file:/path/to/log4j.properties \
  --conf spark.executor.memory=2g \
  --conf spark.driver.memory=1g \
  --conf spark.driver.cores=1 \
  --conf spark.executor.cores=2 \
  --conf spark.executor.instances=5 \
  --conf spark.streaming.kafka.maxRatePerPartition=1000 \
  --conf spark.streaming.backpressure.enabled=true \
  --conf spark.streaming.backpressure.initialRate=1000 \
  --conf spark.streaming.kafka.consumer.cache.maxCapacity=1000 \
  --conf spark.streaming.kafka.consumer.cache.initialCapacity=1000 \
  --conf spark.streaming.kafka.consumer.poll.ms=1000 \
  --conf spark.sql.shuffle.partitions=10 \
  --conf spark.sql.streaming.schemaInference=true \
  --conf spark.sql.streaming.checkpointLocation=$CHECKPOINT_DIR \
  $SCRIPT_LOC >> $LOG_DIR/streaming_log.txt 2>&1
