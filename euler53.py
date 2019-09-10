import math


def combinatorics(n,r):

    c = (math.factorial(n))/(math.factorial(r)*math.factorial(n-r))

    return c


count = 0


for n in range(23,101,1):

    for r in range(1,n+1,1):

        if combinatorics(n,r) > 1000000:
            count += 1

print count