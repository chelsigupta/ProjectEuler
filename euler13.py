import sys
numbers = [int(x) for x in sys.stdin.read().split()]
#finish your entry by pressing ctrl+D

sum = 0

for i in range(0,100,1):
    sum = sum + numbers[i]

#print sum

k = str(sum)

print k[0:10]

