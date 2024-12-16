// TODO: Verify environment variables issue
package com.market
import com.typesafe.config.Config

/**
 * Settings class to load and manage configurations for Cassandra, Kafka, Spark, and schemas.
 * This class uses the Typesafe Config library to read from the application.conf file.
 */
class Settings(config: Config) extends Serializable {

  // Spark settings
  var spark: Map[String, String] = {
    Map(
      "master" -> config.getString("spark.master"),
      "appName" -> config.getString("spark.appName.StreamProcessor"),
      "max_offsets_per_trigger" -> config.getString("spark.max_offsets_per_trigger.StreamProcessor"),
      "shuffle_partitions" -> config.getString("spark.shuffle_partitions.StreamProcessor"),
      "deprecated_offsets" -> config.getString("spark.deprecated_offsets.StreamProcessor")
    )
  }

  // Kafka settings
  var kafka: Map[String, String] = {
    Map(
      "server_address" -> s"${config.getString("kafka.server")}:${config.getString("kafka.port")}",
      "topic_market" -> config.getString("kafka.topics.market"),
      "min_partitions" -> config.getString("kafka.min_partitions.StreamProcessor")
    )
  }

  // Schema file paths
  var schemas: Map[String, String] = {
    Map(
      "trades" -> config.getString("schemas.trades")
    )
  }

  // Cassandra settings
  var cassandra: Map[String, String] = {
    Map(
      "host" -> config.getString("cassandra.host"),
      "keyspace" -> config.getString("cassandra.keyspace"),
      "username" -> config.getString("cassandra.username"),
      "password" -> config.getString("cassandra.password"),
      "trades" -> config.getString("cassandra.tables.trades"),
      "aggregates" -> config.getString("cassandra.tables.aggregates")
    )
  }

  /**
   * Method to print configurations for debugging purposes.
   */
  def printConfigs(): Unit = {
    println("Cassandra Configurations:")
    cassandra.foreach { case (key, value) => println(s"  $key -> $value") }

    println("\nKafka Configurations:")
    kafka.foreach { case (key, value) => println(s"  $key -> $value") }

    println("\nSpark Configurations:")
    spark.foreach { case (key, value) => println(s"  $key -> $value") }

    println("\nSchema File Paths:")
    schemas.foreach { case (key, value) => println(s"  $key -> $value") }
  }
}
