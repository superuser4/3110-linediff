questions = [
    ("What year did WW2 start", "1939"),
    ("2 + 2 = ?", "4"),
    ("What colour does red and blue make:", "purple"),
    ("How many days are there in 1 year?", "365")
]


def run_quiz(questions):
    score = 0

    for q, answer in questions:
        user = input(q + " ").strip().lower()
        if user == answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect")

    return score


print("Starting quiz...")
final_score = run_quiz(questions)

print("Final score:", final_score)
print("Total questions:", len(questions))
