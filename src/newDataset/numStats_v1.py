def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


def count_positive(numbers):
    count = 0
    for n in numbers:
        if n > 0:
            count += 1
    return count


values = [-3, 4, 7, -1, 0, 8, 2]

print("Values:", values)
print("Even numbers:", count_even(values))
print("Positive numbers:", count_positive(values))
