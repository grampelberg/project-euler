# Solution for Project Euler problem 5
# http://projecteuler.net/index.php?section=problems&id=5

q = 20
while 1:
    all = True
    for i in xrange(1,21):
        if q % i != 0:
            all = False
            break
    if all:
        break
    q += 20

print q
