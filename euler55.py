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


def isLychrel(n):

    iter = 0

    while iter < 50:

        t = n + reverse_number(n)
        iter += 1

        if isPalindromic(t):
            return False

        n = t

    return True


count = 0

for i in range(1,10000,1):

    if isLychrel(i):
        count += 1

print count