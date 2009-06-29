# Solution for Project Euler problem 10
# http://projecteuler.net/index.php?section=problems&id=10

def prime(n):
    for i in xrange(int(n ** .5), 1, -1):
        if n % i == 0:
            return False
    return True

total = 5
n = 3
while n < 2000000:
    n += 2
    if prime(n):
        print n
        total += n

print total
