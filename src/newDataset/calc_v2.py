def add(a, b):
     result = a + b       
     return result

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: you cant divide by zero")
        return None
    return a / b

print("Add:", add(5, 3))

print("Multiply:", multiply(5, 3))
print("Divide:", divide(5, 3))
