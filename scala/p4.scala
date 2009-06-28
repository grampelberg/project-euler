// Solution for Project Euler problem 4
// http://projecteuler.net/index.php?section=problems&id=4

println((900 to 1000).flatMap(a => (900 to 1000).map(b => a*b)).
    filter(a => a.toString == a.toString.reverse.toString).
    reduceLeft((a,b) => if (a > b) a else b))
