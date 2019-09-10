import string

with open('p022_names.txt') as f:
    lines = f.read().split(',')
    lines = [i.replace('"', '') for i in lines]

sorted_list = sorted(lines, key = str.upper)

def alphabetical_value(s):
    sum = 0

    for i in s:
        k = string.uppercase.index(i) + 1
        sum += k

    return sum

i = 1
total = 0

for x in sorted_list:

    name_score = i * alphabetical_value(x)
    total += name_score
    i += 1

print total