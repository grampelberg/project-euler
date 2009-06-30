# Solution for Project Euler problem 12
# http://projecteuler.net/index.php?section=problems&id=12

import math

def fac(n):
    q = 0
    print n
    for i in [2, 3, 5, 7, 11, 13]:
        if n % i != 0:
            return
    for i in xrange(1, n+1):
        if n % i == 0:
            q += 1
    print n, q
    return q

n = 1
while fac(sum(xrange(1, n+1))) < 500:
    n += 1
print n
