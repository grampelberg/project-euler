# Solution for Project Euler problem 9
# http://projecteuler.net/index.php?section=problems&id=9

for i in xrange(1, 50):
    for j in xrange(i+1, 50):
        a = 2*i*j
        b = j**2 - i**2
        c = i**2 + j**2
        if (a + b + c) == 1000:
            print a * b * c
            break

