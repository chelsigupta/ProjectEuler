def reverse_number(n):
    rem = 0
    rev_num = 0

    while n>0:
        rem = n%10
        rev_num = rev_num * 10 + rem
        n /= 10

    return rev_num


def isPalindromic(n):

    if n == reverse_number(n):
        return True

    return False


sum = 0

for i in range(1,1000000,1):

    if isPalindromic(i):
        bin_i = bin(i)
        binary_i = int(bin_i[2:])

        if isPalindromic(binary_i):
            print i
            sum += i

print sum