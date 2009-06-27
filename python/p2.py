# Solution for Project Euler problem 2
# http://projecteuler.net/index.php?section=problems&id=2

def fib(limit):
    i = [1, 1]
    while i[-1] + i[-2] < limit:
        i.append(i[-1] + i[-2])
    return i


if __name__ == '__main__':
    print sum([x for x in fib(4000000) if x % 2 == 0])
