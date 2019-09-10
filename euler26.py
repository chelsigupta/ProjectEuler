from __future__ import division


def length_of_recurring_cycle(d):

    map = {}
    deci_pos = 0
    rem = 10

    while True:
        deci_pos += 1
        rem = rem % d

        if rem == 0:
            return 0

        if rem in map:
            i = map[rem]
            return deci_pos - i

        else:
            map[rem] = deci_pos

        rem *= 10


longest_cycle = 0

for d in range(7,1000,1):

    k = length_of_recurring_cycle(d)

    if longest_cycle < k:
        longest_cycle = k


for d in range(7,1000,1):

    if longest_cycle == length_of_recurring_cycle(d):
        print d
        break
