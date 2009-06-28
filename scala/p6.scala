// Solution for Project Euler problem 6
// http://projecteuler.net/index.php?section=problems&id=6

println(pow((1 to 100).reduceLeft(_+_), 2) - (1 to 100).map(a => a.toDouble).reduceLeft((a, b) => a + pow(b, 2)))
