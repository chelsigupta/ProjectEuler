def digit_5th_power_sum(n):
    sum = 0

    while n > 0:

        j = (n % 10)**5
        sum += j
        n /= 10

    return sum


total = 0

for i in range(10,354295,1):

    if i == digit_5th_power_sum(i):
        total += i

print total