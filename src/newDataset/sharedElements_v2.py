#this [program returns the shared elements that exist in 2 seperate strings]

list1 = [1, 20, 41, 50]
list2 = [30, 40, 50, 60]

set_list1 = set(list1)
set_list2 = set(list2)

common_elements = set_list1.intersection(set_list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")

if common_elements == set():
    print(f"There are no comment elements between these sets")
else:
    print(f"Common elements using sets: {common_elements}")