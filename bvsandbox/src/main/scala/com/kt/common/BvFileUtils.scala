package com.kt.common

import java.text.SimpleDateFormat
import java.util.Date
import java.io.{FileWriter, File}
import scala.io._
import org.apache.commons.io.FileUtils
import java.nio.charset.Charset


/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 8:12 AM
 * To change this template use File | Settings | File Templates.
 */


object BvFileUtils {
	private[this] val logger = grizzled.slf4j.Logger[this.type]

	val dateFormat = new SimpleDateFormat("yyyyMMdd-HHmm")

	def appendTimeStamp(baseName: String): String = baseName + "_" + dateFormat.format(new Date)


	def writeStringToFile(fname: String, str: String, append:Boolean = false): String = {

		createMissingPath(fname)

		try {
//			FileUtils.writeStringToFile(ofile, str)
			val writer = new FileWriter(fname, append)
			writer.write(str)
			writer.close()
			"good"
		} catch {
			case e: Exception => "failed to write to: " + fname + "\n" + e.toString
			case _: Throwable => "failed to write to: " + fname
		}

	}


	def createMissingPath(fname: String) {
		//	Make sure parent directory exists, otherwise create it
		val parent = (new File(fname)).getParentFile
		if (!parent.exists()) parent.mkdirs
	}

	def writeListToTSV[T](fname: String,
												toWrite: List[T],
												addTimeStamp: Boolean = true,
												append: Boolean = false,
												header: String = "",
												suffix: String = ".tsv"): String = {
		val ofname = {
			if (addTimeStamp) appendTimeStamp(fname)
			else fname
		} + suffix

		createMissingPath(ofname)

		logger.info("Writing to: " + ofname)

		try {
			val writer = new FileWriter(ofname, append)


			if (header.nonEmpty) writer.write(header + "\n")
			toWrite.foreach(l => writer.write(l + "\n"))
			writer.close()
			"Wrote successfully to: " + ofname
		} catch {
			case e: Exception => "failed to write to: " + ofname + "\n" + e.toString
			case _: Throwable => "failed to write to: " + ofname
		}
	}


}
