import math


def isPrime(n):

    if n%2 == 0:
        return False

    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


def has_4_distinct_prime_factors(n):

    count=0

    if n%2 == 0:
        count+=1
        n /= 2

    i=3
    while(i<=n):

        if n%i==0:

            n /= i

            if isPrime(i):
                count+=1

        if count > 4:
            return False

        i += 2

    if count == 4:
        return True

    return False


num = 210

while True:

    if isPrime(num):
        num=num+1
        continue
    if isPrime(num+1):
        num=num+2
        continue

    if isPrime(num+2):
        num=num+3
        continue

    if isPrime(num+3):
        num=num+4
        continue

    if has_4_distinct_prime_factors(num) and has_4_distinct_prime_factors(num+1) and has_4_distinct_prime_factors(num+2) and has_4_distinct_prime_factors(num+3):
        print num
        break

    num=num+1