f = []

f.append(0)
f.append(1)
f.append(2)
n = 3
d = 0

while d != 1000:

    k = f[n-1] + f[n-2]
    f.append(k)
    d = len(str(k))

    n +=1

print n