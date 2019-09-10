import math


def isPentagonal(n):

    d = math.sqrt(1+24*n)

    r1 = (1+d)/6
    r2 = (1-d)/6

    if r1>0 and math.floor(r1)==r1:
        return True

    if r2>0 and math.floor(r2)==r2:
        return True

    return False


def isHexagonal(n):

    d = math.sqrt(1+8*n)

    r1 = (1+d)/4
    r2 = (1-d)/4

    if r1>0 and math.floor(r1)==r1:
        return True

    if r2>0 and math.floor(r2)==r2:
        return True

    return False


t = 286

while t > 285:

    tn = (t*(t+1))/2

    if isPentagonal(tn) and isHexagonal(tn):
        print tn
        break

    t +=1