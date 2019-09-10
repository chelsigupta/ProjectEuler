total = 1

for i in range(3,1002,2):
    k = i ** 2
    l = k - i + 1
    m = l - i + 1
    n = m - i +1

    sum = k + l + m + n

    total += sum


print total