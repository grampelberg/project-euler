// Solution for Project Euler problem 2
// http://projecteuler.net/index.php?section=problems&id=2

def fib(x: List[Int], y: Int): List[Int] = x match {
  case Nil => error("")
  case i :: Nil => error("")
  case i :: j :: xs => if (i + j < y) fib(i + j :: x, y) else x
}

println(fib(List(1,1), 4000000).reduceLeft((a, b) =>
  if ( b % 2 == 0) a+b else a))
