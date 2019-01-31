import sun.security.tools.PathList

import sbt.Keys._

name := "ICP 2"

version := "0.1"

scalaVersion := "2.11.8"

mainClass in Compile :=Some("ICP 2")

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.1" % "provided",
  "org.apache.spark" %% "spark-streaming" % "1.6.1",
  "org.apache.spark" %% "spark-mllib" % "1.6.1"
)
exportJars := true
fork := true

