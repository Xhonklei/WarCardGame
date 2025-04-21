'''
This is player class which has players main attributes and methods!
'''

class Player:
    def __init__(self,name):
        self.name =name
        self.player_deck =[]

    def add_card(self,new_card):
        #new_card is the card dealt from the main deck
        self.player_deck.append(new_card)
    
    def win_card(self,won_cards):
        #won_cards is a list of cards won by the player
        self.player_deck = won_cards + self.player_deck        

    def remove_card(self):
        # To remove one card from player deck
        return self.player_deck.pop()

    def print_deck(self):
        #To have a view of player deck
        print(f'{self.name} has the following deck:\n')
        for card in self.player_deck:
            print(card)
