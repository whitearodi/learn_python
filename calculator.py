#Build a simple calculator 
# Conditional statements 
# 3 seperate inputs 
#celcius to fahrenheit conversion

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
mode = input("Enter math operation(+, -, *, /): ")

if mode == '+': 
    print(num1 + num2)
elif mode == '-':
    print(num1 - num2)
elif mode == '*':
    print(num1 * num2)
else: 
    print(num1 / num2)

