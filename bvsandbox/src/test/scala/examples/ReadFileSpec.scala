package examples

import org.scalatest.FlatSpec
import org.scalatest.matchers.ShouldMatchers
import com.kt.examples.ReadFile

/**
 * Created with IntelliJ IDEA.
 * User: bvartanian
 * Date: 8/13/13
 * Time: 10:34 AM
 * To change this template use File | Settings | File Templates.
 */
class ReadFileSpec extends FlatSpec with ShouldMatchers {
	"read test" should "read listfile.tsv and print as one line to listfile.tsv_date-time.tsv" in {
		ReadFile.bvReadFile("testoutput/listfile.tsv") should equal ("good")
	}
}
