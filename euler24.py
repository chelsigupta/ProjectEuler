import itertools

lst = [0,1,2,3,4,5,6,7,8,9]

k = list(itertools.permutations(lst))

print k[999999]