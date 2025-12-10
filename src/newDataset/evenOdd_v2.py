#This function divides the numbers in two arrays one of even and other of odd

def evenOdd(numbers):
    odd = []
    even = []
    for number in numbers:
        if (int(number) % 2)  != 0:
            odd.append(number)
        else:
            even.append(number)
    return odd, even

if __name__ == '__main__':
    userInput = input("Enter the numbers (seperated by spaces) to check: ")
    userInput = list(userInput.split())
    odd, even = evenOdd(userInput)
    print('Even Numbers: ', ','.join(even), '\n', 'Odd Numbers: ', ','.join(odd))