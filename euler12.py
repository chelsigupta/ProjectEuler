from itertools import combinations

def count_div(n):
    factors=[]

    start=2
    while(n>0 and start<=n):
        if(n%start==0):
            n=n/start
            factors.append(start)
            start=2
        else:
            start=start+1

    divisors=[]
    for i in range(1,len(factors)+1,1):
        temp=combinations(factors,i)
        for t in temp:
            ex=list(t)
            res=1

            for ee in ex:
                res*=ee
            if(res not in divisors):
                divisors.append(res)

    return len(divisors)+1

n = 1

while True:

    t_num = (n*(n+1))/2

    if count_div(t_num) > 500:
        print t_num
        break

    n += 1