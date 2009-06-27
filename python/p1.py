# Solution for Project Euler problem 1
# http://projecteuler.net/index.php?section=problems&id=1

def mod(x, factors):
    for j in factors:
        if x % j == 0:
            return True

if __name__ == '__main__':
    print sum([x for x in xrange(1000) if mod(x, [3, 5])])
