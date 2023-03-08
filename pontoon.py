import random
from colorama import Fore
from cards import Card


#-------------------------- FUNCTIONS ---------------------------------------------------------------

# To ensure no duplicates of cards - can't have 2 Aces of Clubs!
# Flexible enough to check anyone' hand
def check_card(selected_card, hand):
    card_ok = False

    for i in range (0, len(hand)):
        if selected_card.get_value() == hand[i].get_value() and selected_card.get_suit() == hand[i].get_suit():
            card_ok = False
            break
        else:
            card_ok = True

    if card_ok:
        return True
    else:
        return False

# Deal the requested number of cards
# Can be used to deal the first 2 cards, or just the one, on twist
def deal(hand, no_cards, cp):

    for i in range(no_cards):
       rand_int1 = random.randint(1, 13)
       rand_suit = random.randint(0,3)

       selected_card = Card(suits[rand_suit], (rand_int1) )

       card_OK = check_card(selected_card, hand) # Ensure card has not already been played

       if no_cards == 2: 
           hand.append(selected_card)
           no_cards += 1

       if card_OK:
          hand.append(selected_card)
          if cp == "p":
            show_hand(hand)

          no_cards += 1

    return hand

# Displays the cards 
def show_hand (hand):
    for i in range (0, len(hand)):
        hand[i] .face_up()


# Calculates the total for the hand
def calc_hand_total(hand):
    total = 0
    for i in range (0, len(hand)):
        if hand[i] .get_value() >= 10:
            total += 10
        else:    
            total += hand[i] .get_value()

    return total
  
#-------------------------- INITIALISATION ---------------------------------------------------------------
# Initialise variables
suits = ["hearts", "spades", "diamonds", "clubs"]
player_hand = []
player_total = 0
comp_hand = []
comp_total = 0


#-------------------------- PLAYER'S TURN ---------------------------------------------------------------
# The player's turn
print("Your hand is: ")  
player_hand = deal(player_hand, 2, "p")

# Stick or twist
stick_or_twist = "t"
stick_or_twist = input ("Do you want to stick(s) or twist(t)? ")  
while stick_or_twist.lower() == "t":
    deal (player_hand, 1, "p")
    player_total = calc_hand_total(player_hand)

    if player_total < 22:
        stick_or_twist = input ("Do you want to stick(s) or twist(t)? ")  
    else:    
        print (Fore.RED + "You're bust!")
        stick_or_twist = "s"
        print (Fore.RESET)

player_total = calc_hand_total(player_hand)



#-------------------------- COMPUTER'S TURN ---------------------------------------------------------------
# The computer's turn
print("")
print("It's the computer's turn ...")
input()
comp_hand = deal(comp_hand, 2, "c")
comp_total = calc_hand_total(comp_hand)

# Computer twists
while comp_total < 18:
  print("The computer twists...")
  input()
  comp_hand = deal(comp_hand, 1, "c")
  comp_total = calc_hand_total(comp_hand)

print("The computer sticks")
input()


#-------------------------- SHOW HANDS ---------------------------------------------------------------
# Show player's hand
print(Fore.GREEN + " -------------------- Your hand is hand -------------------- ")
show_hand (player_hand)
print(Fore.GREEN + "Player total ", player_total)
if player_total > 21:
    print (Fore.RED + "You're bust!")
print(Fore.RESET + "")


# Show computer's hand
input()
print("")
print(Fore.CYAN + " -------------------- Computer hand -------------------- ")
show_hand (comp_hand)
print(Fore.CYAN + "Computer total ", comp_total)
if comp_total > 21:
    print (Fore.RED + "Computer is bust!")
print(Fore.RESET + "")


#--------------------------SHOW RESULTS ---------------------------------------------------------------
# Display the results
input()

if player_total > 21 and comp_total > 21:
    print (Fore.RED +"**************************************************************")
    print (Fore.RED + "You're both bust! - No-one wins!")
elif player_total == comp_total:
    print (Fore.WHITE +"**************************************************************")
    print (Fore.WHITE + "The game is a tie")
elif player_total > comp_total and player_total <= 21:
    print (Fore.YELLOW +"**************************************************************")
    print(Fore.YELLOW + "Congratulations  you win !!")
elif  comp_total  > 21:
    print (Fore.YELLOW +"**************************************************************")
    print(Fore.YELLOW + "Congratulations  you win !!")
else:
    print (Fore.CYAN +"**************************************************************")
    print (Fore.CYAN + "The computer wins this time.  Better luck next time!")
print ("**************************************************************")
print()
    
