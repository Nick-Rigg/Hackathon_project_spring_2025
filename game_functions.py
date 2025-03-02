from utils.classes import *

def get_player_choice():
    print('Would you like to Hit (H), Stand (S), Double Down (D), or Split (T)?')
    return input('Player, what would you like to do: ').strip().upper()

def execute_player_turn(player: Player, deck: Deck, bet_amount: int):
    player_score = player.calculate_hand()

    while player_score < 21:
        player_choice = get_player_choice()
        if player_choice == 'H':
            player.add_card(deck.deal())
        elif player_choice == 'D':
            if (bet_amount * 2) > player.bank:
                print('You do not have the funds to double down')
                continue
            player.add_card(deck.deal())
            break
        elif player_choice == 'S':
            break
        player_score = player.calculate_hand()
        print(f'Player score: {player_score}')

    return player_choice, player_score

def execute_dealer_turn(dealer: Dealer, deck: Deck):
    dealer_score = dealer.calculate_hand()
    
    while dealer_score <= 16:
        dealer.add_card(deck.deal())
        dealer_score = dealer.calculate_hand()
        print(f'Dealer score: {dealer_score}')

    return dealer_score

def place_player_bet(bank_balance):
    while True:
        try:
            bet_amount = int(input('Player, place your bet: '))
            if 0 < bet_amount <= bank_balance:
                return bet_amount
            print('Invalid bet. Enter a new betting amount: ')
        except ValueError:
            print('Invalid input. Please enter a number.')

def play_blackjack():
    deck = Deck()
    deck.shuffle()

    dealer = Dealer(deck)
    player = Player(deck)
    bank_balance = player.bank
    bet_amount = place_player_bet(bank_balance)

    # Drawing Cards
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    print(f"Player's score: {player.calculate_hand()}")
    print(f"Dealer's card: {dealer.hand[0]}")

    if player.calculate_hand() == 21:
        print('You hit a blackjack!')
        bank_balance += (1.5 * bet_amount)

    player_choice, player_score = execute_player_turn(player, deck, bet_amount)

    if player_score > 21:
        print('You went over 21!')
        bank_balance -= (2 * bet_amount) if player_choice == 'D' else bet_amount
    else:
        dealer_score = execute_dealer_turn(dealer, deck)

        if player_score > dealer_score or dealer_score > 21:
            print('You win!')
            bank_balance += (2 * bet_amount) if player_choice == 'D' else bet_amount
        elif dealer_score > player_score:
            print('Dealer won!')
            bank_balance -= (2 * bet_amount) if player_choice == 'D' else bet_amount
        else:
            print('You tied!')

    print(f'New balance: {bank_balance}')

def main():
    play_blackjack()

if __name__ == "__main__":
    main()