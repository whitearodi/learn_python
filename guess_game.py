#Build a guess_game 
# Using a while loop
# Guess no 1 to 10
num = input("Enter no: ")
guess_no = 2
i = 0



while i < 3:
    
    if num == guess_no:
        print("Your guess is correct")
        break
    else:
        print("Your guess is incorrect")
        i+=1


   
