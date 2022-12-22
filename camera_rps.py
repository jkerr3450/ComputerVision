import cv2
from keras.models import load_model
import numpy as np
import time
import random 
input 

global wins 
global ties
global losses 
global games_played 

wins = 0
losses = 0
ties = 0
games_played = 0
# List of possible choices in game 
options =  ["rock", "paper", "scissors"]

def countdown():
    seconds = 3 # seconds set to 3  
    while seconds > 0:
        print("start in ...") # While seconds is more than 3, count down 
        print(seconds)
        cv2.waitKey(1500) #cv.2 in milliseconds 
        seconds = seconds - 1
    while seconds < 1:
        print("GO!")    ### added in to gve a short pause before dispalying answer
        cv2.waitKey(1000)
        break 

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    choices_list = ["Rock", "Paper", "Scissors", "Nothing"]

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        user_choice = choices_list[prediction.argmax()]
        np.argmax
        cv2.imshow('frame', frame)
       
        # Press q to close the window
        print(prediction)
        print(f"You have chosen {user_choice}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        countdown()
    
        print(user_choice)
        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)
        print(f"Wins: {wins} Losses {losses} Ties: {ties}")  # to see if code is counting games

        if wins >= 3:
            print(f"You won!. You have won {wins} out of 5 games!")
        if losses >=3:   # losses are wins for the computer 
            print(f"Unlucky. The computer has scored {losses}. Better luck next time!") # states the users no. losses. 
       
        if games_played == 5:
            break 

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

# passed in function from manual rps
def get_computer_choice():
# randomly selects an asnwer from the list and prints it. 
    choice = random.choice(options)
    print(choice)
    return choice

def get_winner(computer_choice, user_choice):       ########
# passed in get winner function from manual rps and added score count 
    global wins, losses, ties, games_played
    user_choice = user_choice.lower()
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}")
        ties += 1           ## adds 1 to win etc 
        games_played += 1   ##  adds 1 to games played 
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Paper beats rock. You lost")
            losses += 1
            games_played += 1 
        else:
            print("Rock beats scissors. You won!")
            wins =+1
            games_played += 1 
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper beats rock. You won!")
            wins += 1
            games_played += 1 
        else:
            print("Scissors beats paper. You lost!")
            losses += 1 
            games_played += 1 
    
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Rock beats scissors. You lost!")
            losses += 1 
            games_played += 1 
        else: 
            print("Scissors beats paper. You won!")
            wins += 1 
            games_played += 1
    else: 
        print("You have lost. Anything beats nothing!")
        losses += 1
        games_played += 1 
    
get_prediction()