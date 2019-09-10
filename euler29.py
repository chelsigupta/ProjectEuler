mylist = []

for a in range(2,101,1):
    for b in range(2,101,1):
        k = a **b

        if k not in mylist:
            mylist.append(k)


print len(mylist)
