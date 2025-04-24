'''
This is the function so solve war conflicts
'''

from GameModules.highest_card import highest_card

def war(game_cards,war_players_pos,all_players):
    '''
    This is the function that it used to solve war stuations on game:
    Each player in war, withdraw 3 cards facedonw and 1 face up
    Face up cards are compared and the winner player takes all the cards

    It takes as arguments:
    1- The cards that brought to the war (list of cards)
    2- Players in the war(in form of positions) (list of positions)
    3- Players in the game (list of players)
    ----------------------------------------------------------
    It returns:
    1- Players remaing in the game
    
    '''
    # First, each player in the war withdraw 3 cards and add to game_cards
    i = 0
    while i < len(war_players_pos):
        # If a player has less than 4 cards to fight the war,
        #  all his cards are taken and he is out of the game
        if len(all_players[war_players_pos[i]].player_deck) < 4:
            while len(all_players[war_players_pos[i]].player_deck) != 0:
                game_cards.append(all_players[war_players_pos[i]].remove_card())
            print(f'{all_players[war_players_pos[i]].name} is out of the game!')
            all_players.remove(all_players[war_players_pos[i]])
            
            #Update the position of players in war, 
            # before removing position of the eliminated player
            for j in range(i+1,len(war_players_pos)):
                war_players_pos[j] -=1
            war_players_pos.pop(i)

        else:
            for m in range(3):
                game_cards.append(all_players[war_players_pos[i]].remove_card())
            i +=1

    # If all players in the war cannot fight it(not enough cards)
    # the war stops with no winner(cards on the game this round are lost).
    if len(war_players_pos) == 0:
        return all_players
    else:
        # Each player in the war withdraw the 4the card 
        # and see who is the winner of this round
        war_cards = []
        for pos in war_players_pos:
            war_cards.append(all_players[pos].remove_card())
        game_cards = game_cards + war_cards # game_cards.extend(war_cards)
        war_win = highest_card(war_cards)

        # If there is a winner he takes all the cards played on that round.
        if len(war_win) == 1:
            print(f'{all_players[war_players_pos[war_win[0]]].name} is the winner of this round!')
            all_players[war_players_pos[war_win[0]]].win_card(game_cards)
            return all_players
        # If there is still war, the same rules of war are followed.
        else:
            # In order to keep the correct track of position when a new war is recalled: 
            # then we pas a list of only the players that are in war,
            #  so that modifications made in war function doesn't affect the main list of players.
            new_all_player =[]
            for pos in war_players_pos:
                new_all_player.append(all_players[pos])
            
            remain_player = war(game_cards,war_win,new_all_player)

            # The list of all players is updated accordingly to the modifications happed in recall
            #  of war function, and finally the all_players list is returned.
            n = 0
            while n < len(new_all_player):
                if new_all_player[n] not in remain_player:
                    all_players.remove(new_all_player[n])
                n +=1

            return all_players