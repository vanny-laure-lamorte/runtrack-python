list= [1,2,3,4,5]

v1 = list[0]

list[0] = list[-1]
list[-1] = v1

print(list)