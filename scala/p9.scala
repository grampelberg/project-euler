// Solution for Project Euler problem 9
// http://projecteuler.net/index.php?section=problems&id=9

import scala.Math._

println((1 to 1000).flatMap(x => (1 to x).
  map(y => List(x, y, (1000-x-y)))).
  filter(x => pow(x.apply(0), 2) + pow(x.apply(1), 2) == pow((1000-x.apply(0)-x.apply(1)), 2)).map(x => x.reduceLeft(_*_)))
