#Using comprehensions involves writing less code.Same as using a for loop

# numbers = [1, 2, 3, 4, 5]
numbers = range(1, 6)
new_list = []

#num is the loop variable that iterates over the list
for num in numbers: 
    new_list.append(num * num)

print(new_list)

# writing a comprehensions 
new_list1 = [ num * num for num in numbers]

print(new_list1)