import math

def digit_fact_sum(N):
    sum = 0

    while N>0:
        d = N%10
        N /= 10
        sum += math.factorial(d)

    return sum


sum = 0

for n in range(10,2540160,1):
    if n == digit_fact_sum(n):
        sum += n

print sum