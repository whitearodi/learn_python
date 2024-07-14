#This script or program involves using while loops 

number = 5
i = 0


while i < 3: 
    guess = int(input("Guess the number mf!! between 1 to 10"))
    if guess == number: 
        print("You have guessed correctly!! ")
        break 
    else: 
        print(f'Incorrect guess. {guess} is not the number ')
        i+= 1
        
if number != guess: 
    print(f'Sorry you loose! The number was {guess}')