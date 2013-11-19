object Hi extends App {
	val now = new org.joda.time.DateTime()
	println("Hi SBT, the time is " + now.toString("hh.mm aa"))
	println("Hello SBT")
}
