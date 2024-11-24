// build.sbt
import sbt.Keys._

val sparkVersion = "3.5.0"

lazy val root = (project in file("."))
  .settings(
    name := "StreamingPreprocessing",
    version := "1.0",
    scalaVersion := "2.12.15",
    
    // Set the main class
    Compile / mainClass := Some("stream-processor"),
    
    // Dependencies
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-core" % sparkVersion,
      "org.apache.spark" %% "spark-streaming" % sparkVersion,
      "org.apache.spark" %% "spark-sql" % sparkVersion,
      "org.apache.spark" %% "spark-streaming-kafka-0-10" % sparkVersion,
      "org.apache.spark" %% "spark-avro" % sparkVersion,
      "com.datastax.spark" %% "spark-cassandra-connector" % sparkVersion,
      "com.datastax.cassandra" % "cassandra-driver-core" % "3.11.3",
      "io.github.cdimascio" % "dotenv-java" % "2.2.4",
      "org.apache.avro" % "avro" % "1.11.3"
    ),
    
    // Remove 'provided' scope for local development
    run / fork := true,
    
    // Add Spark Packages resolver
    resolvers += "Spark Packages Repo" at "https://dl.bintray.com/spark-packages/maven"
  )