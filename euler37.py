import math


def isPrime(n):

    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):
        if n%i == 0:
            return False

    return True


def isTruncatable_left(n):
    s = str(n)

    while len(s)!= 1:
        a = s[:-1]
        k = int(a)

        if k!=2 and (k%2==0 or k == 1):
            return False

        if isPrime(k) == False:
            return False

        s = a

    return True


def isTruncatable_right(n):
    s = str(n)

    while len(s)!= 1:
        a = s[1:]
        k = int(a)

        if k!=2 and (k%2==0 or k == 1):
            return False

        if isPrime(k) == False:
            return False

        s = a

    return True

sum = 0
n = 11
count = 0

while count != 11:
    if isPrime(n):
        if isTruncatable_left(n) and isTruncatable_right(n):
            sum += n
            count += 1
            #print n

    n +=2

print sum