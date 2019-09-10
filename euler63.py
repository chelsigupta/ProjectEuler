count = 0

for p in range(1,100,1):

    for n in range(1,100,1):

        k = n ** p

        if len(str(k)) == p:
            count += 1

print count