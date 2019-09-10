import math


def isPrime(n):
    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


def sum_of_proper_factors(n):
    sum = 0

    for i in range(1,n,1):
        if n%i == 0:
            sum = sum + i

    return sum


mylist = []

for i in range(10000,3,-1):

    k = sum_of_proper_factors(i)

    if sum_of_proper_factors(k)==i and i and k not in mylist and i!=k:
        mylist.append(i)
        mylist.append(k)


print sum(mylist)

