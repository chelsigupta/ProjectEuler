import math


def isPrime(n):
    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


def has_diff_digits(n,t):
    l = []

    while n != 0:
        k = n % 10

        if k in l or k==0 or k > t:
            return False

        l.append(k)
        n /= 10

    return True


for i in range(9876543,3,-2):

    t = len(str(i))

    if has_diff_digits(i,t) and isPrime(i):
        print i
        break