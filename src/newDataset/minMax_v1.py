def find_max(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val

def find_min(nums):
    min_val = nums[0]
    for n in nums:
        if n < min_val:
          min_val = n
    return min_val

numbers = [5, 2, 8, 3, 9, 1]
print("Max:", find_max(numbers))
print("Min:", find_min(numbers))

print("Calculation complete.")

