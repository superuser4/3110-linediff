#this function counts vowels

def countVowels(sentence):
    count = 0
    sentence = sentence.upper()
    for c in sentence:
        if c in ['A', 'E', 'I', 'O', 'U']:
            count += 1
    return count


if __name__ == '__main__':
    userInput = str(input("Enter the string to check for vowels: "))
    count = countVowels(userInput)
    
    if count == 0: 
        print('There are no vowels in your sentence')
    else:
        print('Vowel Count: ',count)