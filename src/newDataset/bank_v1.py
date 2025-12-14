#this program simulates basic bank functions

balance = 0


def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrew:", amount)
    else:
        print("Insufficient funds")


deposit(100)
withdraw(40)
withdraw(80)

print("Final balance:", balance)
