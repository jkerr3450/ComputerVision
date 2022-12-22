import random 
input 

# List of possible choices in game 
options =  ["rock", "paper", "scissors"]

def get_computer_choice():
# randomly selects an asnwer from the list and prints it. 
    choice = random.choice(options)
    print(choice)
    return choice

def get_user_choice():
# Prompts the user to select and answer. 
    user_action = input("Type rock, paper or scissors!")
    user_action = user_action.lower()
    return user_action

# Game code - decides winner based on computer and user selections.
def get_winner(computer_choice, user_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}")

    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Paper beats rock. You lost")
        else:
            print("Rock beats scissors. You won!")
    
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper beats rock. You won!")
        else:
            print("Scissors beat spaper. You lost!")
    
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Rock beats scissors. You lost!")
        else: 
            print("Scissors beats paper. You won!")

    else: 
        print("Please select rock, paper or scissors!")
        

# final funtion that plays game. 
def play():
    computer_choice = get_computer_choice()  ## Fubntion has been assigned to a variable becasue the function definiton contains a return. 
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()