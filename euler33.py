from __future__ import division
from numpy import prod


def is_curious(n,d):
    k = str(n)
    l = str(d)

    m = list(set(k).intersection(l))

    if len(m) == 1:

        if k[0]!=k[1]:
            for i in range(0,2,1):
                if k[i] != m[0]:
                    p = int(k[i])
        else: p = int(m[0])

        if l[0]!=l[1]:
            for i in range(0,2,1):
                if l[i] != m[0]:
                    q = int(l[i])
        else: q = int(m[0])

        if n/d == p/q:
            return True

    return False


N_list = []
D_list = []

for N in range(11,99,1):

    if N%10 != 0:

        for D in range(N+1,100,1):

            if D%10 != 0 and is_curious(N,D):
                N_list.append(N)
                D_list.append(D)


P = prod(N_list)

Q = prod(D_list)

print Q//P