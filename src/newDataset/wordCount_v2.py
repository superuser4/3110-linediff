def analyze_text(text):
    words = text.lower().split()
    total = len(words)
    unique = len(set(words))
    return total, unique


sentence = "this is a simple simple test sentence"

print("Sentence:", sentence)
total, unique = analyze_text(sentence)

print("Total words:", total)
print("Unique words:", unique)
