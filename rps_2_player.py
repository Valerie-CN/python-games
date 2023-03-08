import random
from getpass import getpass

# See who has won when player chooses rock
def check_rock (player2_choice):
    global player_score, player2_score
    if  player2_choice == "paper":
        player2_score += 1
        print ("Paper wraps rock ")
    elif  player2_choice == "rock":
        print ("The game is a tie")
    else:
        player_score += 1
        print (f"Rock blunts scissors")

# See who has won when player chooses paper
def check_paper (player2_choice):
    global player_score, player2_score
    if  player2_choice == "rock":
        player_score += 1
        print (f"Paper wraps rock")
    elif player2_choice == "paper":
        print ("The game is a tie")
    else:
        player2_score += 1
        print ("Scissors cut")

# See who has won when player chooses scissors
def check_scissors (player2_choice):
    global comp_score, player_score
    if  player2_choice == "rock":
        player2_score += 1
        print ("Rock blunts scissors")
    elif player2_choice == "scissors":
        print ("The game is a tie")
    else:
        player_score += 1
        print (f"Scissors cut paper")

# Does the player want to play again
def play_again():
    global player2_score, player_score
    print(f"{player1_name} score - ", player_score)
    print(f"{player2_name} score - ", player2_score)
    print("Computer score - ", comp_score) 
    still_playing = input ("Do you want to play again? ").upper()

    if still_playing == "Y" or still_playing == "YES":
        user_choice = input("Please choose rock, paper or scissors: (n to stop) ").lower()
        return True, user_choice
    else:
        return False, ""


# Main game loop
def main_game (still_playing, user_choice):

    while still_playing:
        
        print ("You have chosen: ", user_choice)

        player2_choice = input("Player 1 - Please choose rock, paper or scissors: (n to stop) ").lower()
    

        if user_choice == "rock":
            check_rock(player2_choice)
            still_playing, user_choice = play_again()
        elif user_choice == "paper":
            check_paper(player2_choice)
            still_playing, user_choice = play_again()
        elif user_choice == "scissors":
            check_scissors(player2_choice)
            still_playing, user_choice = play_again()
        else:
            print ("Plesse enter rock, paper or scissors")




################################################################
# Preparing for the game
################################################################

# Initialise variables
user_choice = ""
still_playing = True
player_score = 0
comp_score = 0
player2_score = 0

# Create the list
play = ["rock", "paper", "scissors"]

#User input
player1_name = input("Player 1, please enter your name: ")
player2_name = input("Player 2, please enter your name: ")

# Ensure the user enters a valid input
while user_choice not in play or user_choice == "" or user_choice == "n" or user_choice == "no":
    user_choice = input("Please choose rock, paper or scissors: (n to stop) ").lower()

############
# Main game
############
main_game (still_playing, user_choice)

#########################################################
# End of the game
#########################################################

# Output the results
print()
print("*******************************************")
print (f"Thanks for plaing {player1_name} and {player2_name}, I hope you had fun!")
print(f"Your score {player1_name} - {player_score}")
print(f"Your score {player2_name} - {player2_score}")


if player_score > player2_score:
    print(f"Congratulations {player1_name} wins !!")
elif player_score == player2_score:
    print (f"The game is a tie - well played {player1_name} and {player2_name}")
else:
    print(f"Congratulations {player2_name} wins !!")

print("*******************************************")
