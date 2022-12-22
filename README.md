# Computer_Vision
AiCore Project 2 - Rock, Paper, Scissors. 

For this project, I will create a game of rock, paper, scissors which will have virtual interaction with the computer. 

## Milestone 2 - Creating The Computer Vision System. 
After setting up the environment and the repository of this project, I then proceeded to create the model on which the game is based. 

For this, I have taken a series of images for each factor in the game - rock, paper, scissors, nothing. 

I have taken around 500 images of each to train my model and allow it to be as accurate as possible. I then downloaded the files that contain the structure and parameters of the game. 

### Milestone 3 - Installing Dependencies

From here, I then downloaded the required dependencies to allow the model to operate correctly. Thus required OpenCV-python, tensorflow, and ipykernel. 



## Milestone 4 - Create a Rock, Paper, Scissors Game. 
Firstly, I downloaded the template which housed the code that allowed the user to pick a choice using the webcam. After passing my model into the code, I was able to finish the design of the game. 

For this, I coded two functions. "get_computer_choice" and "get_winner". The computer choice function allows for a random choice from the list of R, P or S. The choice is then displayed.

```def get_computer_choice():```
 ```choice = random.choice(options)```
 ```print(choice)```
 ```return choice```


The get-winner function allows the code to decide who has won the round. To do this, I used the basic rules of the game - paper beats rock, scissors beats paper etc. 
Each choice also adds to the list of wins, losses and ties. This was straightforward as each deciding factor was coded in if & Elif blocks. 

 if user_choice == computer_choice:
 print(f"It's a tie! You both chose {user_choice}")
 ties += 1 
 games_played += 1 
 elif user_choice == "rock":
 if computer_choice == "paper":
 print("Paper beats rock. You lost")
 losses += 1
 games_played += 1 

The game will then display the score and who the winner is. 

Now that the basics of the are created, I had to create the main body, where the game was played - "get_prediciton". 

For this, I have added to the template which was installed in the previous milestone. 

As the template had the code which allowed the users choice to be predicted through np.array, I added multiple functions to allow the game to play in full. 

For example - "coutndown()". the countdown function slows the game down. Using the cv2.waitKey function, I added a pause of 1.5 seconds between each game. 

For this, I added code to the template that was downloaded in the previous milestone. The template is the code that allows the user to pick a choice through the camera, based on my model, which is then framed, resized and then out through a NumPy array - a grid of values. 

```def countdown():```
 ```seconds = 3 # seconds set to 3``` 
 ``` while seconds > 0:```
 ```print("start in ...")```
 ```print(seconds)```
 ```cv2.waitKey(1500) #cv.2 in milliseconds`` 
 ```seconds = seconds - 1``
 ```while seconds < 1:```
 ```print("GO!")```
 ``` cv2.waitKey(1000)```
 ```break```

To add to the user experience, I added some basic formulas that will end the game once 5 games have been played. From here, it will display the wins, losses & ties. 
Depending on the value of wins or losses, it will display a message of congratulations or ask you to try again. 