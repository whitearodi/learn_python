name = input("Input your name: ")
distance = input("Input your distance: ")
calculation = int(distance) / 1.069
miles = round(calculation,1)
print("Hi " + name.capitalize() + " this the distance you covered in " + distance + " in km" + 
" & in miles " + str(miles) + " miles")