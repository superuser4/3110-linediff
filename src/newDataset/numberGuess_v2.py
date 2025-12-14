import random

# this function randomly chooses a number from 0-30

def guess():
    randomNumber = random.randint(0, 31)
    count = 0

    while True:
        count += 1
        number = int(input('Guess the number between 0 to 30 within 4 attempts: '))
        if count <= 4:
            if number < randomNumber:
                print('Too small')
            elif number > randomNumber:
                print('Too large')
            else:
                print('You have got it in', count, 'tries')
                break
        else: 
            print('Uh oh! Too many attempts')
            break

if __name__ == '__main__':
    guess()