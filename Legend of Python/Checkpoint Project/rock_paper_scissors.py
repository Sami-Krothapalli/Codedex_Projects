import random

## Title Page:
print(" =================== \n Rock Paper Scissors \n =================== \n")

print("Welcome to Rock Paper Scissors! \n")
print("1.) ✊")
print("2.) ✋")
print("3.) ✌️")

## User Input:
user_choice = int(input("Enter your choice: "))

##Computer Choice:
computer_choice = random.randint(1, 3)

def user_choice_Print(user_choice):
    if user_choice == 1:
        print("You chose: ✊")
    elif user_choice == 2:
        print("You chose: ✋")
    elif user_choice == 3:
        print("You chose: ✌️")

def computer_choice_Print(computer_choice):
    if computer_choice == 1:
        print("Computer chose: ✊")
    elif computer_choice == 2:
        print("Computer chose: ✋")
    elif computer_choice == 3:
        print("Computer chose: ✌️")


## Game Logic:
# Display choices for the user and computer
if user_choice == computer_choice:
    user_choice_Print(user_choice)
    computer_choice_Print(computer_choice)
    print("It's a tie!")
elif user_choice == 1 and computer_choice == 2:
    print("You chose: ✊")
    print("Computer chose: ✋")
    print("You lose!")
    print("The Computer won!")

elif user_choice == 1 and computer_choice == 3:
    print("You chose: ✊")
    print("Computer chose: ✌️")
    print("You win")
    print("The player won!")
## User Choice 2
elif user_choice == 2 and computer_choice == 1:
    print("You chose: ✋")
    print("Computer chose: ✊")
    print("You win!")
    print("The player won!")
elif user_choice == 2 and computer_choice == 3:
    print("You chose: ✋")
    print("Computer chose: ✌️")
    print("You loose!")
    print("The Computer won!")

## User Choice 3
elif user_choice == 3 and computer_choice == 1:
    print("You chose: ✌️")
    print("Computer chose: ✊")
    print("You loose!")
    print("The Computer won!")

elif user_choice == 3 and computer_choice == 2:
    print("You chose: ✌️")
    print("Computer chose: ✋")
    print("You win!")
    print("The player won!")
else:
    print("Invalid input. Please try again.")

