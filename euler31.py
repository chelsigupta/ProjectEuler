denoms = [1,2,5,10,20,50,100,200]

DP = [0] * 201
DP[0] = 1

for K in range(0,8,1):
    co = denoms[K]
    for n in range(co,201,1):
        DP[n] = DP[n] + DP[n-co]

print DP[200]