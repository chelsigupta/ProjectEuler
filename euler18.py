n = 15
main_list=[]

for i in range(0,n,1):

    temp = [int(x) for x in raw_input().split()]
    main_list.append(temp)

i = n-2

while i >= 0:
    temp_u = main_list[i]
    temp_l = main_list[i+1]

    for x in range(0,len(temp_u),1):

        temp_u[x] += max(temp_l[x],temp_l[x+1])

    i -= 1

print main_list[0]