// Solution for Project Euler problem 1
// http://projecteuler.net/index.php?section=problems&id=1

println((1 to 1000).filter{ i => (i % 3 == 0) || (i % 5 == 0)}.reduceLeft(_+_))
println( (0 to 1000).reduceLeft( (a, b) =>
  if ( (b % 3 == 0) || (b % 5 == 0) ) a+b else a) )
