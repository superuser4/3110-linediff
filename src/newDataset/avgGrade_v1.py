#this program gets the average student grade

def calculate_average(grades):
    total = 0
    for g in grades:
        total += g
    return total / len(grades)


def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


grades = [85, 90, 78, 92, 88]
average = calculate_average(grades)

print("Grades:", grades)
print("Average:", average)
print("Letter Grade:", get_letter_grade(average))
