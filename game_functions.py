from utils.classes import *

def get_player_choice():
    print('Would you like to Hit (H), Stand (S), Double Down (D)?')
    return input('Player, what would you like to do: ').strip().upper()

def execute_player_turn(player: Player, deck: Deck, bet_amount: int):
    player_score = player.calculate_hand()
    has_hit = False

    while player_score < 21:
        player_choice = get_player_choice()
        if player_choice == 'H':
            player.add_card(deck.deal())
            has_hit = True
        elif player_choice == 'D':
            if has_hit:
                print('You cannot double down after hitting.')
                continue
            if (bet_amount * 2) > player.bank:
                print('You do not have the funds to double down.')
                continue
            player.add_card(deck.deal())
            print('You have doubled down and received one more card.')
            player_score = player.calculate_hand()
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

def play_blackjack(player: Player, dealer: Dealer, deck: Deck):
    bet_amount = place_player_bet(player.bank)

    # Drawing Cards
    for _ in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    print(f"Player's score: {player.calculate_hand()}")
    print(f"Dealer's card: {dealer.hand[0]}")

    if player.calculate_hand() == 21:
        print('You hit a blackjack!')
        player.bank += (1.5 * bet_amount)
    else:
        player_choice, player_score = execute_player_turn(player, deck, bet_amount)

        if player_score > 21:
            print('You went over 21!')
            player.bank -= (2 * bet_amount) if player_choice == 'D' else bet_amount
        else:
            dealer_score = execute_dealer_turn(dealer, deck)

            if player_score > dealer_score or dealer_score > 21:
                print(f'You win! player: {player_score}, dealer: {dealer_score}')
                player.bank += (2 * bet_amount) if player_choice == 'D' else bet_amount
            elif dealer_score > player_score:
                print(f'Dealer won! dealer: {dealer_score}, player: {player_score}')
                player.bank -= (2 * bet_amount) if player_choice == 'D' else bet_amount
            else:
                print('You tied!')

    print(f'New balance: {player.bank}')

def main():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player(deck)
    bank_amount = player.bank
    print(f'You start with: {bank_amount} dollars')
    
    while bank_amount > 0:
        player.reset_hand()
        dealer.reset_hand()
        deck.reset_deck()
        deck.shuffle()
        play_blackjack(player, dealer, deck)
        bank_amount = player.bank

if __name__ == "__main__":
    main()