package com.kt.examples

import java.io.FileReader
import scala.io.{BufferedSource, Source}
import com.kt.common.BvFileUtils

/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 10:24 AM
 * To change this template use File | Settings | File Templates.
 */
object ReadFile {
	def bvReadFile(fname: String): String = {
		val file: BufferedSource = Source.fromFile(fname)
		val input = file.getLines().toList
		file.close()
		val asString = input.mkString(",")
		println(asString)
		BvFileUtils.writeListToTSV(fname, List(asString), header = "my junk header")
		"good"
	}
}
