# Solution for Project Euler problem 6
# http://projecteuler.net/index.php?section=problems&id=6

print sum(xrange(1, 101))**2 - reduce(lambda a, b: a + b**2, xrange(1, 101))
