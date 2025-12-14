#this program simulates basic bank functions

balance = 0


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        return False 
    balance -= amount
    return True


deposit(100)

if not withdraw(40):
    print("Withdrawal failed")

if not withdraw(80):
    print("Withdrawal failed")

print("Balance:", balance)
