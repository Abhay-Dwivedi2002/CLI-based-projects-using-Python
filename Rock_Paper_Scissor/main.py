
# Rock Paper Scissor game witth computer 

'''
WORLFLOW OF PROJECT:
1- Input from user (Rock , Paper , Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print


Cases :

A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win


B- Paper

Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win


C- Scissor

Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Paper win

'''

import random
iterm_list  = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter your move =  Rock, Paper, Scissor = ")
comp_choice = random.choice(iterm_list)

print(f"User choice = {user_choice}, Computer Choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both chooses same : = Match Tie")

elif user_choice == "Rock" :
    if comp_choice == "Paper":
        print("Paper covers Rock , Computer wins")
    else:
        print("Rock smashes Scissor , You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper , Computer wins")
    else:
        print("Paper covers Rock , You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper , You win")
    else:
        print("Rock smashes Scissor , Computer wins")







