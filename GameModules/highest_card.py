'''
The function to find the player/s with highest card of the round
'''

def highest_card(game_cards):
    '''
    This function takes as input a list of cards 
    that were withdrawn by each player during a round.
    -------------------------------------------------
    It returns a list of the position/s of player/s
    with the highest card value
    '''
    card_values = []
    winners = []
    # First extract the value of each player's card
    for card in game_cards:
        card_values.append(card.value)

    # Find the highest value 
    max_val = max(card_values)
    pos = 0
    # Keep a record of the position of each player
    # that has the card with highest value
    for card in game_cards:
        if card.value == max_val:
            winners.append(pos)
        pos +=1
    # Return the list of positions
    return winners