package com.kt.common

import org.scalatest.matchers.ShouldMatchers
import org.scalatest.FlatSpec
import java.text.SimpleDateFormat
import java.util.Date

/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 8:19 AM
 * To change this template use File | Settings | File Templates.
 */
class FileUtilsSpec extends FlatSpec with ShouldMatchers {
	"junk" should "give junk_date-time" in {
		val dateFormat = new SimpleDateFormat("yyyyMMdd-HHmm")
		FileUtils.appendTimeStamp("junk") should
			equal("junk" + "_" + dateFormat.format(new Date))
	}

	"test writer" should "write 'nothing' to nada.txt" in {
		val str = "nothing"
		val fname = "../../nada.txt"
		FileUtils.writeStringToFile(str, fname)
	}
}
