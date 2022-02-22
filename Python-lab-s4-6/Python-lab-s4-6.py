#Python programme to print sum of all numbers in a list

list = [10,20,30,40,60]
add=0

for i in range(len(list)):
        add += list[i]


print(list)
print("sum of list: ",sum(list))