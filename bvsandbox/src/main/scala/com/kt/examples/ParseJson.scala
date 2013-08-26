package com.kt.examples

import scala.io.{Source, BufferedSource}
import com.kt.common.BvFileUtils
import java.io.{FileWriter, File}

/**
 * Use main to convert the double quoted json object to single quotes.
 * Still doesn't parse the json object.
 * First I need to separate out the json, and then write the entire list + each
 * 	entry in the json object
 */

object ParseJson {

	def getBaseExt(name: String): (String, String) = {
		val lastDot = name.lastIndexOf(".")
		if (lastDot >= 0) (name.substring(0, lastDot), name.substring(lastDot))
		else (name, "")
	}

	def createNameWithTime(name: String): String = {
		val (base, ext) = getBaseExt(name)
		BvFileUtils.appendTimeStamp(base) + ext
	}

	def removeExtraChars(s: String) = {
		val pat = """[\"]""".r
		pat.replaceAllIn(s.trim, "").toString
	}

	def convertStuff(s: String) = {
		val pat1 = """(\"\{\")""".r
		val pat2 = """(\"\}\")""".r
		val pat3 = """(\":\")""".r
		val pat4 = """(\"\",\"\")""".r
		pat4.replaceAllIn(pat3.replaceAllIn(pat2.replaceAllIn(pat1.replaceAllIn(s, "{"), "}"), ":"), """","""")
	}

	def convertDoubleQuoteToEscaped(s: String) = {
		val pat = """[\"\"]""".r
		pat.replaceAllIn(s.trim, """\"""")
	}

	def examineEvtJson(fname: String) = {

		val file: BufferedSource = Source.fromFile(fname)
		val lines = file.getLines().toList
		file.close()

		//		println("raw file")
		//		lines.foreach(l => println(l))
		//
		//		println("after stripping quotes")
		//		lines.foreach(l => println(removeExtraChars(l)))
		//
		//		println("after converting to list")
		//		lines.foreach(l => {
		//			val curline = removeExtraChars(l)
		//			println(curline.split(","))
		//		}
		//		)

		val ofname = createNameWithTime(fname)

		try {
			val writer = new FileWriter(ofname)

			println("after convertStuff")
			lines.foreach(l => {
				val curline = convertStuff(l)
				writer.write(curline + "\n")
			})
			writer.close()
		} catch {
			case e: Exception => "failed to write to: " + ofname + "\n" + e.toString
			case _: Throwable => "failed to write to: " + ofname
		}

	}

	def main(args: Array[String]) {
//		val fname = "/Users/bvartanian/Development/wbi/challenge-analysis/data/raw/with-json-r.csv"
		val fname = "/Users/bvartanian/Development/wbi/challenge-analysis/sql/sample-data.csv"
		val file = new File(fname)
		val parent = file.getParentFile
		val filename = file.getName

		examineEvtJson(fname)
	}
}
