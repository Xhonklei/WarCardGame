'''
The function to evenly split cards between players!
'''

def split_deck(deck, list_of_players):
    '''
    This function takes the playing deck and a list of players who are playing
    and split the cards evenly between the players
    '''
    # First we make sure that there is at least a remaining card for each player
    while len(deck) >= len(list_of_players):
        #For each player that is playing, we take a card from main deck
        #and add it to the individual player's deck
        for i in range(len(list_of_players)):
            list_of_players[i].add_card(deck.deal_one())