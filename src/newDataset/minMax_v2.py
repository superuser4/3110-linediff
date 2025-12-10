numbers = [5, 2, 8, 3, 9, 1]

def find_max(nums):
    max_val = nums[0]         
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

def find_min(nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min

print("Maximum:", find_max(numbers)) 
print("Minimum:", find_min(numbers))  


print("Done.")
