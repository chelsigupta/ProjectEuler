n1 = 577
d1 = 408
count = 0

for i in range(8,1001,1):

    n2 = n1 + 2*d1
    d2 = n1 + d1

    if len(str(n2)) > len(str(d2)):
        count += 1

    n1 = n2
    d1 = d2

print count