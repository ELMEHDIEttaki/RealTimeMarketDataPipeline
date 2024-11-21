
lazy val root = (project in file(".")).
  settings(
    name := "StreamingPreprocessing",
    version := "1.0",
    scalaVersion := "2.12.15"
  )

val sparkVersion = "3.5.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-streaming" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-sql" % sparkVersion % "provided",
  "org.apache.spark" %% "spark-streaming-kafka-0-10" % sparkVersion % "provided",
  "com.datastax.spark" %% "spark-cassandra-connector" % sparkVersion % "provided",
  "com.datastax.cassandra" % "cassandra-driver-core" % "3.11.3" % "provided"
)

addSbtPlugin("nl.gn0s1s" % "sbt-dotenv" % "3.1.0")