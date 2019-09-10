import math


def isPrime(n):

    if n%2==0 and n!=2:
        return False

    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


def count_of_cons_primes(a,b):
    n = 0
    count = 0

    while True:
        t = (n*n) + (a*n) + b

        if isPrime(abs(t)) == False:
            break

        count += 1
        n += 1

    return count


maximum = 0

for a in range(-999,1000,1):

    for b in range(-1000,1001,1):

        k = count_of_cons_primes(a,b)

        if k > maximum:
            maximum = k
            prod = a*b

print prod