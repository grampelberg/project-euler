// Solution for Project Euler problem 5
// http://projecteuler.net/index.php?section=problems&id=5

def gcd(a: Long, b: Long): Long = b match {
  case 0 => a
  case _ => gcd(b, a % b)
}

println((1 to 20).map(a => a.toLong).reduceLeft((a, b) => a*b/gcd(a, b)))
