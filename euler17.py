a = [0]*1001

a[0] = 0
a[1] = len('one')
a[2] = len('two')
a[3] = len('three')
a[4] = len('four')
a[5] = len('five')
a[6] = len('six')
a[7] = len('seven')
a[8] = len('eight')
a[9] = len('nine')
a[10] = len('ten')
a[11] = len('eleven')
a[12] = len('twelve')
a[13] = len('thirteen')
a[14] = len('fourteen')
a[15] = len('fifteen')
a[16] = len('sixteen')
a[17] = len('seventeen')
a[18] = len('eighteen')
a[19] = len('nineteen')
a[20] = len('twenty')
a[30] = len('thirty')
a[40] = len('forty')
a[50] = len('fifty')
a[60] = len('sixty')
a[70] = len('seventy')
a[80] = len('eighty')
a[90] = len('ninety')



for i in range(21,100,1):
    u = i%10
    t = i-u

    if u!=0:
        a[i] = a[t] + a[u]


hund = len('hundred')
vand = len('and')

for i in range(100,1000,1):
    h = i/100
    tu = i%100

    if tu!=0:
        a[i] = a[h] + hund + vand + a[tu]

    else:
        a[i] = a[h] + hund

a[1000] = len('onethousand')

sum = 0
for i in range(1,1001,1):
    sum = sum + a[i]

print sum