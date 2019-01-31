import org.apache.spark.{SparkConf, SparkContext}

object ICP2 {
  def main(arg: Array[String]){

    System.setProperty("hadoop.home.dir","C:\\Users\\Tondi\\Dropbox\\COMP SCI 5542\\winutils");

    val sparkConf = new SparkConf().setAppName("ICP 2").setMaster("local[*]")

    val sc = new SparkContext(sparkConf)

    val input =sc.textFile("input")

    val text = input.flatMap(line=>{line.split(" ")}).map(word=>(word.charAt(0), word + " ")).cache()

    val output = text.reduceByKey(_+_)

    output.saveAsTextFile("output")
    
  }
}