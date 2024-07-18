# import modules 
import time as t
import random as rd 
# ask how many questions user wants 
no_questions = int(input("How many questions do you want? "))
max_num = int(input("Highest number used in practice"))

# set score at zero
score = 0
answer_list = []
start = t()
# loop through the number of questions 
for q in range(no_questions):
    num1,num2 = rd.randrange(1,max_num+1), rd.randrange(1,max_num+1)
    ans = num1 * num2
    u_ans = input(f'{num1} X {num2} = ')
    answer_list.append(f'{num1} X {num2} = {ans} you:{ans}')
    if u_ans == ans: 
        score+=1
    end = t()
print(f"""Thank you for playing
You got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct
in {round((end-start)/no_questions, 1)} seconds/questions""")

for a in answer_list:
    print(a), 

#Create random numbers & cal answer 
#Show user the question
# capture answer & modify user score 
# Output final score 