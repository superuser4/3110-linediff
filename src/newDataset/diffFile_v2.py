#this is an age checker

x = int(input("Enter your age: "))
if x < 18 :
    print("MINOR")
elif x <= 65 :
    print("ADULT")
else :
    print("SENIOR")