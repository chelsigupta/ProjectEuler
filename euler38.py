def has_diff_digits(n):
    l = []

    while n != 0:
        k = n % 10

        if k in l or k==0:
            return False

        l.append(k)
        n /= 10

    return True


maximum = 0

for num in range(2,987655,1):
    k = 0
    prod = str(num)

    if has_diff_digits(num):
        n = 2

        while len(prod)!= 9:

            prod = prod + str(num * n)

            if has_diff_digits(int(prod)) == False:
                k = 1
                break

            n += 1
            
    if k == 0 and int(prod) > maximum:
        maximum = int(prod)

print maximum