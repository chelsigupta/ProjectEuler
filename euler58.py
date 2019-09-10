import math


def isPrime(n):

    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


diag_count = 13
prime_count = 8
percent = 62
s = 7

while True:
    s += 2
    diag_count += 4

    k = (s ** 2) - s + 1
    l = k - s + 1
    m = l - s + 1

    if isPrime(k):
        prime_count += 1

    if isPrime(l):
        prime_count += 1

    if isPrime(m):
        prime_count += 1

    percent = math.ceil((prime_count*100)/diag_count)

    if percent < 10:
        print s
        break