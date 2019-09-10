def has_diff_digits(n):
    l = []

    while n != 0:
        k = n % 10

        if k in l or k==0:
            return False

        l.append(k)
        n /= 10

    return True


diff_digit_numbers = []

for i in range(1,9876,1):

    if has_diff_digits(i) == True:
        diff_digit_numbers.append(i)


def isPandigital_1to9(s):

    if len(s)==9 and has_diff_digits(int(s)) == True:
        return True

    return False


final_list = []

for i in range(0,len(diff_digit_numbers),1):

    mu = len(str(diff_digit_numbers[i]))
    if mu > 2:
        break

    for j in range(0,len(diff_digit_numbers),1):

        ml = len(str(diff_digit_numbers[j]))

        if (mu==2 and ml==3)or(mu==1 and ml==4):
            k = diff_digit_numbers[i] * diff_digit_numbers[j]

            if k in diff_digit_numbers:

                s = str(k)+str(diff_digit_numbers[i])+str(diff_digit_numbers[j])

                if isPandigital_1to9(s) == True and k not in final_list:
                    final_list.append(k)


print sum(final_list)