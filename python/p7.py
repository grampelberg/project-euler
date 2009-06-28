# Solution for Project Euler problem 7
# http://projecteuler.net/index.php?section=problems&id=7

# i = 3
# q = [2]
# while len(q) < 10001:
#     prime = True
#     for j in q:
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         q.append(i)
#     i += 2

# print q[-1]

def prime(n):
    for i in xrange(int(n ** .5), 1, -1):
        if n % i == 0:
            return False
    return True

count = 2
n = 3
while count < 10001:
    n += 2
    if prime(n):
        count += 1
print n
