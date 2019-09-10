def is_abundant(n):
    sum = 0

    for i in range(n-1,1,-1):
        if n%i == 0:
            sum += i
        if sum > n:
            return True

    return False


mylist = []

for i in range(12,28124-12,1):
    if is_abundant(i):
        mylist.append(i)

mylist2 = []

for i in range(0,len(mylist),1):

    for j in range(i,len(mylist),1):

        k = mylist[i] + mylist[j]
        if k > 28123:
            break

        mylist2.append(k)


y = list(set(mylist2))
print y
t = sum(y)
m = (28123*28124)/2

print m-t