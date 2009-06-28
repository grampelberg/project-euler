// Solution for Project Euler problem 7
// http://projecteuler.net/index.php?section=problems&id=7

import scala.Math._

def prime(n: Int): Boolean =
  if ( (2 to pow(n, .5).toInt).reverse.filter(x => n % x == 0).length == 0 )
    true
  else
    false

def nextprime(n: Int): Int = n match {
  case x if prime(x) => x
  case x => nextprime(x + 2)
}

lazy val primes: Stream[Int] = Stream.cons(3, primes.map(x => nextprime(x + 2)))

// Seeded with the 2nd prime
println(primes.apply(10001 - 2))

