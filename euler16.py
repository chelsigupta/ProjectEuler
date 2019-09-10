n = 2 ** 1000
sum = 0

while n!=0:
    k = n%10
    sum = sum + k
    n /= 10

print sum
