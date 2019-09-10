def digit_sum(n):
    sum = 0

    while n!=0:
        k = n%10
        sum = sum + k
        n /= 10

    return sum


max_sum = 0

for a in range(2,100,1):

    for b in range(1,100,1):

        k = a ** b
        l = digit_sum(k)

        if max_sum < l:
            max_sum = l

print max_sum