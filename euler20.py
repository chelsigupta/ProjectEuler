fact = 1

for i in range(1,101,1):
    fact = fact*i

sum = 0

while fact!=0:
    k = fact%10
    sum = sum +k
    fact /= 10

print sum
