with open('p079_keylog.txt') as f:
    lines = f.read().splitlines()

lst = [[] for i in range(10)]

for i in lines:
    k = int(i[0])

    if int(i[1]) not in lst[k]:
        lst[k].append(int(i[1]))

    if int(i[2]) not in lst[k]:
        lst[k].append(int(i[2]))

    l = int(i[1])

    if int(i[2]) not in lst[l]:
        lst[l].append(int(i[2]))

max_len = 0

for i in lst:
    if max_len < len(i):
        max_len = len(i)

number = []
while max_len > 0:

    for i in range(0,10,1):
        if len(lst[i]) == max_len:
            number.append(i)

    max_len -= 1

for i in lst:
    if len(i) == 1:
        number.append(i[0])

print number


