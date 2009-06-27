// Solution for Project Euler problem 3
// http://projecteuler.net/index.php?section=problems&id=3

def factor(num: Long, fac: Int): Int = num match {
  case 1 => fac
  case x => if (x % fac == 0) factor(x/fac, fac) else factor(x, fac+1)
}

println(factor(600851475143L, 2))
