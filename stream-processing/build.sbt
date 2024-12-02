// stream-processing/build.sbt

val sparkVersion = "3.5.0"

ThisBuild / version := "1.0.0"
ThisBuild / scalaVersion := "2.12.15"
ThisBuild / organization := "com.market"

lazy val root = (project in file("."))
  .settings(
    name := "stream-processing",
    
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-core" % sparkVersion,
      "org.apache.spark" %% "spark-streaming" % sparkVersion,
      "org.apache.spark" %% "spark-sql" % sparkVersion,
      "org.apache.spark" %% "spark-streaming-kafka-0-10" % sparkVersion,
      "org.apache.spark" %% "spark-avro" % sparkVersion,
      "com.datastax.spark" %% "spark-cassandra-connector" % sparkVersion,
      "com.datastax.cassandra" % "cassandra-driver-core" % "3.11.3",
      "io.github.cdimascio" % "dotenv-java" % "2.2.4"
    ),

    Compile / run / mainClass := Some("com.market.StreamingPreprocessingApp"),
    assembly / mainClass := Some("com.market.StreamingPreprocessingApp"),
    
    
    run / fork := true

  )

//enablePlugins(SbtAvro)
//avroVersion := "1.12.0"



// Assembly settings
assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x                             => MergeStrategy.first
}