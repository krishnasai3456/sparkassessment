# Spark Technical Interview Readme

## Exercise Overview

In the upcoming interview, we will discuss a use case involving the development of a streaming application using Apache Spark. While we are not seeking a fully working example, we aim to understand your approach. The exercise consists of the following components:

### Use Case

1. Create a Spark Structured Streaming pipeline (using Python or Scala) to publish data to Kafka.
2. Use Spark Structured Streaming (Python or Scala) to read the same data from Kafka and store it in HDFS Parquet format in the RAW Zone. You can use any sample XML data with nested elements.
3. Read data from the RAW Zone using an hourly scheduled Spark Batch process and load the final Parquet files into the Processed Zone.

### Output Data Requirements

To demonstrate your approach, consider the following organizational structure:

- Create a sample project folder structure for code (e.g., scripts, logs, etc.).
- Provide sample scripts (pseudo code) and place them in the corresponding folders.

### Code Considerations

In your code, address the following aspects:

- Consume data from Kafka (including Offset Maintenance and De-duplication).
- XML Parsing and flattening.
- Data Validation (Static and Dynamic).
- Schema Validation.
- Data Type Validation.
- Data formatting (e.g., trimming).

### Fault Tolerance for Application

Ensure your code accounts for the following aspects:

- Error Handling.
- Continuous Streaming.
- Checkpoint Restarts from a specific checkpoint.

### Data Partitioning

Partition the data based on a date field in the final Parquet files stored in the Processed Zone.

## Expectations

In this interview, we expect to see pseudo code only. Specifically:

- Provide the main Shell Script (`spark-submit`).
- Share the pseudo code for the Python/Scala Spark program.

Refer to online resources such as GitHub, Google, Spark documentation, or any other Spark sources for guidance in completing this assignment. We are interested in understanding your approach, the functions/methods you intend to use, and the reasoning behind your choices. We do not require a fully functioning code example.

## Additional Topics for Discussion

During our discussion, we may touch upon the following topics:

- How do you ensure that only delta/new records are pulled from the RAW Zone to the Processed Zone?
- What strategies will you employ to manage older data in the RAW Zone to prevent it from becoming too large?
- Will you run these programs on a cluster or as a client?
- How will you determine the appropriate number of cores and executors for:
   - Spark Streaming Job
   - Hourly Spark Batch Job
- How will you avoid encountering the small file issue in both the RAW and Processed Zones?
