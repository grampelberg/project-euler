# Solution for Project Euler problem 4
# http://projecteuler.net/index.php?section=problems&id=4

def reverse_gen(a, b):
    for i in reversed(xrange(900, a)):
        for j in reversed(xrange(900, b)):
            yield i, j

q = 0
for i, j in reverse_gen(1000, 1000):
    prod = str(i * j)
    if prod == prod[::-1] and i*j > q:
        q = i * j

print q


