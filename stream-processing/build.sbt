
// build.sbt
import sbt.Keys._

lazy val root = (project in file("."))
  .settings(
    name := "StreamingPreprocessing",
    version := "1.0",
    scalaVersion := "2.12.15",
    
    // Avro settings
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-core" % sparkVersion % "provided",
      "org.apache.spark" %% "spark-streaming" % sparkVersion % "provided",
      "org.apache.spark" %% "spark-sql" % sparkVersion % "provided",
      "org.apache.spark" %% "spark-streaming-kafka-0-10" % sparkVersion % "provided",
      "org.apache.spark" %% "spark-avro" % sparkVersion % "provided",
      "com.datastax.spark" %% "spark-cassandra-connector" % sparkVersion % "provided",
      "com.datastax.cassandra" % "cassandra-driver-core" % "3.11.3" % "provided",
      "nl.gn0s1s" % "sbt-dotenv" % "3.1.0"
    )

    // Avro source directory configuration
    //Compile / avroSource := baseDirectory.value / "src" / "main" / "avro",
    //Compile / sourceGenerators += (Compile / avroScalaGenerateSpecific).taskValue
    
    // Optional: specify Java source compatibility if needed
    // javacOptions ++= Seq("-source", "1.8", "-target", "1.8"),
    
    // Add Avro specific settings
    // avroSpecificSourceDirectory := baseDirectory.value / "src" / "main" / "avro",
    // avroSpecificScalaSource := baseDirectory.value / "src" / "main" / "streaming-processing"
  )

val sparkVersion = "3.5.0"

// Add resolver for Spark packages
resolvers += "Spark Packages Repo" at "https://dl.bintray.com/spark-packages/maven"