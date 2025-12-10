#This function divides the numbers in two arrays one of even and other of odd

def evenOdd(numbers):
    even = []
    odd = []
    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

if __name__ == '__main__':
    userInput = input("Enter the numbers (seperated by spaces) to check: ")
    userInput = list(userInput.split())
    even, odd = evenOdd(userInput)
    print('Even Numbers: ', ','.join(even), '\n', 'Odd Numbers: ', ','.join(odd))