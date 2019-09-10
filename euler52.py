def has_same_digits(l,m,n,o,p,q):

    if sorted(str(l)) == sorted(str(str(m))) == sorted(str(str(n))) == sorted(str(str(o))) == sorted(str(str(p))) == sorted(str(str(q))):
        return True

    return False


x = 13

while True:

    if len(str(6*x)) == len(str(5*x)) == len(str(4*x)) == len(str(3*x)) == len(str(2*x)) == len(str(x)):

        if has_same_digits(6*x,5*x,4*x,3*x,2*x,x):
            print x
            break

    x +=1