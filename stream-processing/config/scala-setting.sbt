name := "StreamingPreprocessing"

version := "1.0"

scalaVersion := "2.13.12"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.5.0",
  "org.apache.spark" %% "spark-streaming" % "3.5.0",
  "org.apache.spark" %% "spark-sql" % "3.5.0",
  "org.apache.spark" %% "spark-streaming-kafka-0-10_2.12" % "3.5.0",
  "com.datastax.spark" %% "spark-cassandra-connector_2.12" % "3.5.0"
)

libraryDependencies += "me.gosimple" % "dotenv-scala" % "3.0.0"