import random

# See who has won when player chooses rock
def check_rock (comp_choice, name):
    global comp_score, player_score
    if  comp_choice == "paper":
        comp_score += 1
        print ("Paper wraps rock - Computer wins")
    elif comp_choice == "rock":
        print ("The game is a tie")
    else:
        player_score += 1
        print (f"Rock blunts scissors - {name} wins")

# See who has won when player chooses paper
def check_paper (comp_choice, name):
    global comp_score, player_score
    if  comp_choice == "rock":
        player_score += 1
        print (f"Paper wraps rock  - {name} wins")
    elif comp_choice == "paper":
        print ("The game is a tie")
    else:
        comp_score += 1
        print ("Scissors cut - Computer wins")

# See who has won when player chooses scissors
def check_scissors (comp_choice, name):
    global comp_score, player_score
    if  comp_choice == "rock":
        comp_score += 1
        print ("Rock blunts scissors - Computer wins")
    elif comp_choice == "scissors":
        print ("The game is a tie")
    else:
        player_score += 1
        print (f"Scissors cut paper  - {name} wins")

# Does the player want to play again
def play_again():
    global comp_score, player_score
    print(f"{name} score - ", player_score)
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

        comp_choice = play[random.randint(0,2)]
        print ("The computer has chosen :", comp_choice)

        if user_choice == "rock":
            check_rock(comp_choice, name)
            still_playing, user_choice = play_again()
        elif user_choice == "paper":
            check_paper(comp_choice, name)
            still_playing, user_choice = play_again()
        elif user_choice == "scissors":
            check_scissors(comp_choice, name)
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

# Create the list
play = ["rock", "paper", "scissors"]

#User input
name = input("Please enter your name: ")

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
print (f"Thanks for plaing {name}, it was great fun!")
print(f"Your score {name} - {player_score}")
print(f"Computer score - {comp_score}")

if player_score > comp_score:
    print(f"Congratulations {name} you win !!")
elif player_score == comp_score:
    print (f"The game is a tie - well played {name}")
else:
    print ("The computer wins this time.  Better luck next time!")

print("*******************************************")
