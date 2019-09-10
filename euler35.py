import math


def isPrime(n):
    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True

def isCircularPrime(i):
    k = str(i)
    n = 0

    while i!=n:
        a = k[-1] + k[:-1]
        n = int(a)

        if n%2 == 0:
            return False

        if i==n:
            break

        if isPrime(n) == False:
            return False
        k = a

    return True


count = 4

for i in range(11,1000000,2):
    if isPrime(i):
        if isCircularPrime(i):
            count +=1


print count