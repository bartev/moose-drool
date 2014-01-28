/**
 * Created with IntelliJ IDEA.
 * User: bartev
 * Date: 11/9/13
 * Time: 2:55 PM
 * To change this template use File | Settings | File Templates.
 */

val x = 5
Math.pow(x, 3)


(1 to 4).map(Math.pow(2, _))




(1 to 4).map(Math.pow(2, _)).foldLeft(0.0){(a, b) => a + b}



def fibonacci(num:Int): Int = {
  num match {
    case 0 => 0
    case 1 => 1
    case _ => fibonacci(num - 1) + fibonacci(num - 2)
  }
}

fibonacci(5)

def fib_tail(num:Int):Unit = {
  def tail(num:Int, next:Int, res:Int):Int = num match {
    case 0 => res
    case _ => tail(num - 1, next + res, next)
  }
  print(tail(num, 1, 0))
  print(' ')
}

fib_tail(5)

//def fib(num:Int): Unit = {
//  num match {
//    case 0 => print(0)
//    case 1 => print(1)
//    case _ =>
//      var first = 0
//      var sec = 1
//      for i
//
//  }
//}










