#This script involves adding user input then creating a fn that prints out your name 
name = input("What is your name: ")
age = input("Enter your age: ")

#Defined our fn 
# With string formatting you don't need to add the str fn when changing an integer 
def greetings():
    print(f'Hello {name} your age is {age}')

#Call the fn
greetings()