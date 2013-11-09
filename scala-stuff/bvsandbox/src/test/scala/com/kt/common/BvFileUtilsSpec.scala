package com.kt.common

import org.scalatest.matchers.ShouldMatchers
import org.scalatest.FlatSpec
import java.text.SimpleDateFormat
import java.util.Date
import org.apache.commons.io.FileUtils

/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 8:19 AM
 * To change this template use File | Settings | File Templates.
 */
class BvFileUtilsSpec extends FlatSpec with ShouldMatchers {
	"junk" should "give junk_date-time" in {
		val dateFormat = new SimpleDateFormat("yyyyMMdd-HHmm")
		BvFileUtils.appendTimeStamp("junk") should
			equal("junk" + "_" + dateFormat.format(new Date))
	}

	"test writer" should "write to bvsandbox/testoutput/nada.txt" in {
		val fname = "testoutput/nada.txt"
		val str = "nothing"
		BvFileUtils.writeStringToFile(fname, str) should
			equal("good")
	}

	"tsv write test" should "write a list of items to file: listfile.tsv" in {
		val ls = List("hello", "this", "is", "great")
		val path = "testoutput/"
		println(BvFileUtils.writeListToTSV(path + "listfile", ls, addTimeStamp = false, header = "-- no time stamp"))
		println(BvFileUtils.writeListToTSV(path + "listfile", ls, addTimeStamp = true, header = "header text -- with time stamp"))
	}
}
