def count_words(text):
    words = text.split()
    return len(words)


def count_unique_words(text):
    words = text.split()
    return len(set(words))


sentence = "this is a simple simple test sentence"

print("Sentence:", sentence)
print("Word count:", count_words(sentence))
print("Unique words:", count_unique_words(sentence))
