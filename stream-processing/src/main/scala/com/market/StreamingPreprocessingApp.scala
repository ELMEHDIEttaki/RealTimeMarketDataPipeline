/*
import io.github.cdimascio.dotenv.Dotenv
import org.apache.spark.SparkConf
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds


object StreamingPreprocessingApp {
  def main(args: Array[String]): Unit = {
    // Load the .env file
    val dotenv = Dotenv.load()

    // Retrieve environment variables
    val sparkMasterUrl = dotenv.get("SPARK_MASTER_URL")
    val appName = dotenv.get("APP_NAME")
    val kafka_server = dotenv.get("BROKER_URL")
    val kafka_topic = dotenv.get("KAFKA_TOPIC")

    // Configure Spark
    val conf = new SparkConf()
      .setMaster(sparkMasterUrl)
      .setAppName(appName)

    val ssc = new StreamingContext(conf, Seconds(10))

    // Example log message
    println(s"Spark App: $appName running on $sparkMasterUrl")

    // Your Spark Streaming code here

    // Read data from Kafka topic
    val kafkaStream = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", kafka_server)
      .option("subscribe", kafka_topic)
      .load()
    println(s"Display incoming data from market topic: $kafkaStream")
    ssc.start()
    ssc.awaitTermination()
  }
}
**/

// src/main/streaming-processing/StreamingPreprocessingApp.scala

package com.market

import org.apache.spark.sql.{SparkSession, DataFrame}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.avro._
import org.apache.spark.sql.types._
import io.github.cdimascio.dotenv.Dotenv
import java.nio.file.{Files, Paths}
import scala.io.Source

object StreamingPreprocessingApp {
  def loadAvroSchemaFromFile(schemaPath: String): String = {
    try {
      new String(Files.readAllBytes(Paths.get(schemaPath)))
    } catch {
      case e: Exception =>
        println(s"Error loading schema file: ${e.getMessage}")
        throw e
    }
  }

  def main(args: Array[String]): Unit = {
    // Load environment variables
    val dotenv = Dotenv.load()
    
    // Configuration parameters
    val kafkaServer = dotenv.get("BROKER_URL")
    val kafkaTopic = dotenv.get("KAFKA_TOPIC")
    val schemaPath = dotenv.get("AVRO_SCHEMA_PATH")
    val checkpointLocation = dotenv.get("CHECKPOINT_LOCATION")
    val SparkAppName = dotenv.get("APP_NAME")
    val MasterUrl = dotenv.get("SPARK_MASTER_URL")

    // Initialize Spark Session
    val spark = SparkSession
      .builder
      .master("spark://172.20.0.4:7077")
      .appName(SparkAppName)
      .config("spark.sql.streaming.checkpointLocation", checkpointLocation)
      .getOrCreate()
    
    println("Spark session created successfully")

    import spark.implicits._

    // Load Avro schema
    val avroSchema = loadAvroSchemaFromFile(schemaPath)
    
    // Configure error handling
    spark.conf.set("spark.sql.streaming.stopGracefullyOnShutdown", "true")

    try {
      // Create streaming DataFrame from Kafka
      val kafkaStream = spark
        .readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", kafkaServer)
        .option("subscribe", kafkaTopic)
        .option("startingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()

      // Decode Avro messages
      val decodedStream = kafkaStream
        .select(
          col("key").cast("string"),
          from_avro(col("value"), avroSchema).as("data")
        )
        .select("data.*")

      // Add processing timestamp
      val processedStream = decodedStream
        .withColumn("processing_timestamp", current_timestamp())

      // Write the stream to console (for testing)
      val query = processedStream
        .writeStream
        .outputMode("append")
        .format("console")
        .option("truncate", "false")
        .start()

      // Add shutdown hook
      sys.addShutdownHook {
        println("Gracefully stopping Spark Streaming application...")
        query.stop()
        spark.stop()
      }

      println("Application running... Press CTRL+C to exit")
      Thread.sleep(Long.MaxValue)

      // Wait for the streaming query to terminate
      query.awaitTermination()

    } catch {
      case e: Exception =>
        println(s"Error in streaming application: ${e.getMessage}")
        e.printStackTrace()
        spark.stop()
        System.exit(1)
    }
  }
}
