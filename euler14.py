def length_of_chain(n):
    count = 1

    while n > 1:

        if n%2 == 0:
            n = n/2
            count += 1

        if n%2 != 0 and n != 1:
            n = 3*n + 1
            count += 1

    return count


longest_chain = 0

for n in range(2,10**6,1):
    k = length_of_chain(n)

    if longest_chain < k:
        longest_chain = k
        num = n

print num