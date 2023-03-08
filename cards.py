class Card:

    # Initialise the card
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # ---------- VALUE ---------------
    # To be able to change the value of the card e.g. is Jack, Queen, King
    def set_value (self,value):
        self.value  = value  

        # To get the value of the card e.g. 10 for Jack, Queen, King
    def get_value (self):
        return self.value
    
    #--------- SUIT ------------------
    # To be able to change the suit, if required (no used in this game)
    def set_suit (self, suit):
        self.suit = suit 

    # To get the suit of the card (not used in this game)
    def get_suit (self):
        return self.suit
        
    # To convert value to words for some cards
    def face_up(self) :
        if self.value == 1:
            word_value = "Ace"
        elif self.value == 11:
            word_value = "Jack"
        elif self.value == 12:
            word_value  = "Queen"
        elif self.value == 13:
            word_value = "King"
        else:
            word_value = self.value    
        
        return (print (f"{word_value} of {self.suit}"))


