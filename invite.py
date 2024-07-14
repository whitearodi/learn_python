# this program involves using a for loop 
#Didn't exactly need to use nested loop

names = ['john Cleese ', 'Eric IDLE', 'michael']
names1 = ['graham chapman', 'TERRY', 'terry jones']

names.extend(names1)
#Using print statement to debug 
# print(names)

n = input("Add a name to the invitation list: ")
names.append(n)
# print(names)



for list in names:
    print(f'{list.title()}! You are invited to the Sato party')
   
# Lmao over engineering at its best
#     for n1 in names1:
#         # names1.lower()
#         n1 = input("Add a name to the second invitation list")
#         names1.append(n1)
#         print(f'{n1.title()}! You are invited to the Sato party')

    