#this program gets the average student grade

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


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

print("Grades:", grades)
avg = calculate_average(grades)
print("Average:", round(avg, 2)) 
print("Letter Grade:", get_letter_grade(avg))
