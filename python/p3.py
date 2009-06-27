# Solution for Project Euler problem 3
# http://projecteuler.net/index.php?section=problems&id=3

i = 2
f = 600851475143
roots = []
while f > 1:
    if f % i == 0:
        f /= i
        roots.append(i)
        continue
    i += 1
print roots
