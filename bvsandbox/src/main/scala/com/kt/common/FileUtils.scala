package com.kt.common

import java.text.SimpleDateFormat
import java.util.Date
import java.io.FileWriter

/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 8:12 AM
 * To change this template use File | Settings | File Templates.
 */


object FileUtils {
	private[this] val logger = grizzled.slf4j.Logger[this.type]

	val dateFormat = new SimpleDateFormat("yyyyMMdd-HHmm")

	def appendTimeStamp(baseName: String): String = baseName + "_" + dateFormat.format(new Date)

	def writeStringToFile(toWrite: String, fname: String) {
		try {
			val writer = new FileWriter(fname, false)
			writer.write(toWrite)
			writer.close()
		} catch {
			case e: Exception => "failed to write to: " + fname + "\n" + e.toString
			case _: Throwable => "failed to write to: " + fname
		}
	}
}
