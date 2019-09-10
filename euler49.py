import math
import itertools


def isPrime(n):

    if n%2 == 0:
        return False

    for i in range(3,int(math.ceil(math.sqrt(n)))+1,2):

        if n%i == 0:
            return False

    return True


def all_distinct_perms(s):
    t = []

    for x in s:
        t.append(x)

    l = list(itertools.permutations(t))

    dis_perms = []

    for x in l:
        num = 0

        if (int(x[0]) == 0):
            continue

        for i in range(0,len(x),1):
            num = num + int(x[i])*(10 ** (len(x)-1-i))

        if num not in dis_perms:
            dis_perms.append(num)

    return dis_perms


def double_available(li):
    res=[];
    res.append(0)
    for l in li:
        if(l==0):
            continue;
        temp1=l*2;
        temp2=l/2;
        if(temp1 !=0 and temp2 !=0 and (temp1 in li or temp2 in li)):
            res.append(l);
            res.append(temp);
            continue;
        li[li.index(l)]=-1;

    if len(res)==1:
        return []

    return li;



main_list = []


for i in range(1000,9999,1):

    L = []
    if isPrime(i):
        K = all_distinct_perms(str(i))
        t = 0

        for j in K:
            if isPrime(j):
                L.append(j)



    if len(L) >= 3:
        for ll in L:
            temp=[]
            for kk in L:
                temp.append(ll-kk)
            temp=double_available(temp);
            if len(temp)>0 :
                break;

        for i in range(0,len(temp),1):
            if temp[i]!=-1:
                if L[i] not in main_list:
                    main_list.append(L[i])


print main_list


