// Solution for Project Euler problem 10
// http://projecteuler.net/index.php?section=problems&id=10

import scala.Math._

def prime(n: Long): Boolean =
  if ( (2 to pow(n, .5).toInt).reverse.filter(x => n % x == 0).length == 0 ) {
    println(n)
    true
  } else
    false

def nextprime(n: Long): Long = n match {
  case x if prime(x) => x
  case x => nextprime(x + 2)
}

lazy val primes: Stream[Long] = Stream.cons(3, primes.map(x => nextprime(x + 2)))

// Seeded with the 2nd prime
println(primes.takeWhile(x => x < 2000000).reduceLeft(_+_) + 2)
