
#this program will convert temperature in celsius to fahrenheit and vice versa

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return round((f - 32) * 5/9, 2)

temps_c = [0, 10, 21, 30]
temps_f = []

for temp in temps_c:
    temps_f.append(c_to_f(temp))

print("Celsius values:", temps_c)
print("Converted:", temps_f)

print("Back to Celsius:")
for temp in temps_f:
    print(f_to_c(temp))