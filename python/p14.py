# Solution for Project Euler problem 14
# http://projecteuler.net/index.php?section=problems&id=14

def num(n):
    if n % 2:
        return (3*n + 1)/2
    return n/2

def seq(n):
    p = n
    q = 1
    while n != 1:
        if n % 2:
            q += 2
            n = (3*n + 1)/2
        else:
            q += 1
            n = n/2
    print (q, p)
    return (q, p)

print reduce(lambda x,y: x if x[0] > y[0] else y, [seq(i) for i in xrange(2, 1000000)])
