import itertools
l = list(itertools.permutations([1,0,2,3,4,5,6,7,8,9]))


def property(i):

    i_6 = i/10000
    if i_6%10 != 0 and i_6%10 != 5:
        return False

    i_4 = i_6/100

    if i_4%2 != 0:
        return False

    i_5 = i_6/10
    i_3 = i_5/100

    if (i_3%10 + i_4%10 + i_5%10)%3 != 0:
        return False

    i_7 = i/1000
    i_8 = i/100

    if (i_6%10 + i_8%10 - i_7%10)%11 != 0:
        return False

    if (i_7%1000)%7 != 0:
        return False

    i_9 = i/10

    if (i_9%1000)%13 != 0:
        return False

    if (i%1000)%17 != 0:
        return False

    return True


sum = 0

for x in l:
    num = 0
    if x[0] == 0:
        continue

    for i in range(0,len(x),1):
        num = num + x[i]*(10 ** (len(x)-1-i))

    if property(num):
        print num
        sum += num

print sum



