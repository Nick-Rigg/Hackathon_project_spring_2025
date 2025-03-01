from utils.classes import *




def black_jack_game():
    dealer = Dealer()
    player = Player()
    dealer_score = 0
    player_score = 0
    deck = Deck()
    deck.shuffle()

    # Player Bet
    player_bet = int(input('Player, place your bet: '))

    # Dealer Not Bet

    # Drawing Cards
    
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    
    # Player Up
    # Dealer Up
    # Player Up
    # Dealer Down

    

    # Do you want to hit or stand
    # hit = str(input('\nPlayer, do you wish to hit or stand (H/S): ')).upper()

    while True:
        player_option = str(input('\nPlayer, do you wish to hit or stand (H/S): ')).upper()
        if player_option == 'H':
            print('bruh')
            # Player Draw Card Function
        else:
            break

    # Dealer Draws
    while True:
        if dealer_score <= 16:
            print(str(dealer_score) + '\n')
            dealer_score+=1
        else:
            break
    print(str(dealer_score) + '\n')

    # Betting -> Player Up -> Dealer Up -> Player Up -> Dealer Down
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