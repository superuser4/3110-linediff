
#this program will convert temperature in celsius to fahrenheit and vice versa

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return round((f - 32) * 5/9, 2)

temps_c = []
temps_f = [32, 50, 69.8, 86]

for temp in temps_f:
    temps_c.append(f_to_c(temp))

print("Fahrenheit values:", temps_f)
print("Converted:", temps_c)

print("Back to Fahrenheit:")
for temp in temps_c:
    print(c_to_f(temp))