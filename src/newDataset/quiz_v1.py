questions = {
    "What year did World War 2 start": "1939",
    "2 + 2 = ?": "4",
    "What colour does red and blue make:": "Purple",
    "How many days are there in 1 year?": "365",
    "What month is Christmas celebrated in?" : "December",
    "Who is the famous author of 'Romeo and Juliet'" : "William Shakespear",
    "How many degrees is a full circle" : "360",
    "What season do pumpkins get associated with" : "Fall"
}


def ask_question(question, answer):
    user = input(question + " ")
    if user.strip().lower() == answer.lower():
        print("Correct")
        return True
    else:
        print("Incorrect")
        return False


score = 0

for q in questions:
    if ask_question(q, questions[q]):
        score += 1

print("Final score:", score)
print("Out of:", len(questions))
