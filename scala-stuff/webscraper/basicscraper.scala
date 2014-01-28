// import org.apache.log4j.{Level, Logger, BasicConfigurator}
import org.jsoup.nodes.Document

val ??? = "non implemented"
object BasicScraper {
  // BasicConfigurator.configure()
  // val logger: Logger = Logger.getLogger(BasicScraper.getClass)
  // Logger.getRootLogger.setLevel(Level.INFO)

  val baseUrl = "http://www.healthgrades.com/hospital-directory"
  var outputFile = "/Users/bartev/Development/moose-drool/scala-stuff/webscraper/oput.csv"

  def main(args: Array[String]): Unit = {
    val stateList = getListOfStateUrls()
    println(s"stateList = $stateList")

    outputFile = if (args.length > 0) args(0) else outputFile
    println(s"outputFile = $outputFile")

    val cityList = getAllCityUrls(stateList)
    val hospMap = getHospFromCityList(cityList)
    
    println("hospMap.size = $hospMap.size")
    writeHospToFile(hospMap, outputFile)
  }

  def getListOfStateUrls(): List[String] = {
    (Array("")).toList
    // TODO
  }
  
  def getAllCityUrls(sl: List[String]):List[String] = {
  	sl
  	// TODO
  }
  
  def getHospFromCityList(cl: List[String]):Map[String, String] = {
  	(cl map (x => x -> x)).toMap
  	// TODO
  }
  
  def writeHospToFile(hm: Map[String, String], fname:String):Unit = {
  	// TODO
  }
}

val bs = BasicScraper
bs.main(Array())
