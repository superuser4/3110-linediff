#removes the duplicate numbers in a list and maintains order

def removeDuplicate( li ):
    seen = {}  
    for item in li:
        if item not in seen:
            seen[item] = True
            yield item

li = [12,24,35,24,88,120,155,88,120,155]
ans = list(removeDuplicate(li))
print(ans)