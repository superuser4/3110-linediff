#print the first half values in one line and the last half values in one line

tuple = (1,2,3,4,5,6,7,8,9,10)
lst1,lst2 = [],[]

for i in range(0,5):
    lst1.append(tuple[i])

for i in range(5,10):
    lst2.append(tuple[i])

print(lst1)
print(lst2)