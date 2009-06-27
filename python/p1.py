# Solution for Project Euler problem 1
# http://projecteuler.net/index.php?section=problems&id=1

def multiple_sum(limit, multiples):
    sums = 0
    for i in xrange(limit):
        for j in multiples:
            if i % j == 0:
                sums += i
                continue
    return sums

if __name__ == '__main__':
    print multiple_sum(1000, [3, 5])
