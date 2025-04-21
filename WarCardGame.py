"""
Created on Sat Apr 19 22:45:35 2025

@author: Xhonklei
"""

from GameModules.deck_class import Deck 
from GameModules.player_class import Player
from GameModules.split_deck import split_deck
from GameModules.highest_card import highest_card
from GameModules.war import war


def war_card_game():

     # Create the deck of the game and shuffle it.
     mydeck =Deck()
     mydeck.shuffle_deck()

     # Take the number of playing, and their names.
     num_of_players = int(input('Enter the number of players: '))
     players =[]
     for i in range(num_of_players):
          name = input(f"Enter the name of player{i+1}: ")
          players.append(Player(name))

     # Split the deck evenly to all players.
     split_deck(mydeck,players)

     game_on = True
     i = 1 
     while game_on and i != 500: # A limit of 500 rounds is set!
          # For each round print number of cards each player has!
          print(f'\nRound {i}:')
          for player in players:
               print(f'{player.name} has {len(player.player_deck)} cards on his deck.')
          
          # Now each player draw a card from their deck.
          game_cards=[]
          k = 0
          while k < len(players):
               # Here it is checked if the player has cards left on his deck.
               # If not, he is removed from the game!
               if len(players[k].player_deck) == 0:
                    print(f'{players[k].name} is out of the game!')
                    players.pop(k)
               else:
                    game_cards.append(players[k].remove_card())
                    k+=1

          # Here we check if it's only one player in the game, then game over!
          if len(players) == 1:
               print("Game Over!")
               print(f'{players[0].name} is the winner!')
               break

          # To have an idea of cards drew by each player in this round!
          print('Cards in play this round are:')
          for card in game_cards:
               print(card)

          # Get positions of players with the highest card of the round
          winner_pos=highest_card(game_cards)
          print(winner_pos)
          
          # If there is only one player with the highest card,
          #  then he is the winner of this round.
          if len(winner_pos) == 1:
               print(f'{players[winner_pos[0]].name} is the winner of this round!')
               players[winner_pos[0]].win_card(game_cards)
          # If there are more than one player, then we have war.
          else:
               players = war(game_cards, winner_pos, players)
                    
          i += 1

if __name__ == '__main__':
    war_card_game()