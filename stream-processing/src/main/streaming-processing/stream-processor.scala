
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
