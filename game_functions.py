from utils.classes import *


def player_turn(player: Player, deck: Deck):
    player_score = player.calculate_hand()
    print(player_score)

    while True and player_score < 21:
        player_option = str(input('\nPlayer, do you wish to hit or stand (H/S): ')).upper()
        if player_option == 'H':
            player_hand = player.add_card(deck.deal())
            player_score = player.calculate_hand()
            print(f'player score: {player_score}')
        else:
            break

    return player_score


def dealer_turn(dealer: Dealer, deck: Deck):
    dealer_score = dealer.calculate_hand()
    print(f'dealer score: {dealer_score}')

    # Dealer Draws
    while True:
        if dealer_score <= 16:
            dealer_hand = dealer.add_card(deck.deal())
            dealer_score = dealer.calculate_hand()
            print(f'dealer score: {dealer_score}')
        else:
            return dealer_score





def black_jack_game():
    dealer = Dealer(deck=Deck())
    player = Player(deck=Deck())
    deck = Deck()
    deck.shuffle()
    bank = player.bank
    player_bet = int(input('Player, place your bet: '))

    # Drawing Cards
    for _ in range(2):
        player_hand = player.add_card(deck.deal())
        dealer_hand = dealer.add_card(deck.deal())
    
    print(f'Players card: {player_hand[0]}, {player_hand[1]}')
    print(f'Dealers card: {dealer_hand[0]}, card 2 is hidden')


    players_draw = player_turn(player, deck)
    
    if players_draw > 21:
        print('You went over 21!')
        bank -= player_bet
        print(f'new balance: {bank}')
    else:
        dealers_draw = dealer_turn(dealer, deck)
        
        if players_draw > dealers_draw:
            print('You win')
            bank += player_bet
            print(f'new balance: {bank}')
        elif dealers_draw > players_draw:
            print('Dealer won')
            bank -= player_bet
            print(f'new balance: {bank}')
        else:
            print('You tied!')
            print(f'You have the same balance: {bank}')





    # Stand (Player is done, dealer draws) 
    # Hit (Player draws until stand or bust, then dealer draws) ->
    # Double Down (Player doubles bet but draws only 1 card, then dealer draws) ->
    # Split (If players has 2 of the same number cards, player can play 2 hands and choose stand hit or double down for each individual one, then dealer draws) ->

    # Dealer stands on 17 or above
    # Bust is over 21
    # Ace can be 1 or 11

    # Player has a limit on how much money they can lose before they lose the game
    # This can change depending on the boss (e.g. 1st: all money, 2nd: 3/4 of money, 3rd: 1/2 of money)




def main():
    black_jack_game()

if __name__ == "__main__":
    main()