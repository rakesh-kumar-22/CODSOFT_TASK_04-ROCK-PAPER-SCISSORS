# Task-04 Rock-Paper-Scissors Game

import random
print("******* WELCOME TO ROCK - PAPER - SCISSORS GAME ")
count=1
round=1
user_score=0
computer_score=0
while(count):
    print("Round",round," Begins ")
    user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))

    if user_choice >=3 or user_choice <0:
        print("You Entered invalid number ,you lose.")

    else:
        computer_choice=random.randint(0,2)
        print("Computer choice is: ")
        print(computer_choice)

        if computer_choice == user_choice:
            print("It's a draw.")

        elif computer_choice ==0 and user_choice==2:
            print("You loose.")
            computer_score +=1

        elif user_choice ==0 and computer_choice==2:
            print("You win .")
            user_score +=1

        elif computer_choice > user_choice:
            print("You loose.")
            computer_score +=1

        elif user_choice > computer_choice:
            print("You win.")
            user_score +=1

        
        print("Enter 1 if you want to continue and 0 if you want to exit.")
        choice=int(input())
        if choice >=2 or choice <0:
            print("Please select a valid option.")

        else:
            if choice==1:
                count=1
                round+=1

            else:
                count=0

print("The final score are : ")
print("User : ",user_score)
print("Computer : ",computer_score)
if(user_score > computer_score):
    print("User wins")

elif(user_score==computer_score):
    print("There is a tie.")

else:
    print("computer wins")

