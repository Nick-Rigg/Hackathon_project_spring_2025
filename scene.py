import pygame
from globals import *
from sprite import Entity       #, SuperEntity
from text import TextEntity
from game_functions import *
from utils.classes import *

class Scene:
    
    def __init__(self, app) -> None:
        self.app = app
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(deck=self.deck)
        self.player = Player(deck=self.deck)
        
        # card_texture = pygame.image.load('textures/Club2.png').convert_alpha()
        # card_texture = pygame.transform.scale(card_texture, (100, 100))
        font = pygame.font.SysFont('Arial', 64)
        # screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        position = (20, 20)
        text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
       "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
       "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
       "text will disappear underneath the surface"
        
        hit_button_texture = pygame.image.load('textures/HitUnpressStandard.png').convert_alpha()
        hit_button_texture = pygame.transform.scale(hit_button_texture, (200, 200))
                                                    
        stand_button_texture = pygame.image.load('textures/StandUnpress.png').convert_alpha()
        stand_button_texture = pygame.transform.scale(stand_button_texture, (200, 200))
                                                    
        double_double_button_texture = pygame.image.load('textures/DoubleDownUnpress.png').convert_alpha()
        double_double_button_texture = pygame.transform.scale(double_double_button_texture, (200, 200))

        hit_button_inverted_texture = pygame.image.load('textures/HitUnpressInverted.png').convert_alpha()
        hit_button_inverted_texture = pygame.transform.scale(hit_button_inverted_texture, (200, 200))
                                                    
        # stand_button_again_texture = pygame.image.load('textures/StandUnpress.png').convert_alpha()
        # stand_button_again_texture = pygame.transform.scale(stand_button_again_texture, (200, 200))
        
        #-------Testing-------#

        dealer = Dealer(deck=Deck())
        player = Player(deck=Deck())
        deck = Deck()
        deck.shuffle()

        for _ in range(2):
            player_hand = player.add_card(deck.deal())
            dealer_hand = dealer.add_card(deck.deal())

        # print(f'Players card: {player_hand[0]}, {player_hand[1]}')
        # print(player_hand[0])
        # print(player_hand[1])



        # suit = player_hand[0].get_suit()
        # rank = player_hand[0].get_rank()
        # texture_name = (suit + rank + '.png')

        # card_texture = pygame.image.load('textures/' + texture_name).convert_alpha()
        # card_texture = pygame.transform.scale(card_texture, (100, 100))

        #---------------------#

        

        # self.sprites = pygame.sprite.Group()
        #self.start_buttons = pygame.sprite.Group()
        # self.text = pygame.sprite.Group()

        # self.entity = Entity([self.sprites])
        # self.text = TextEntity([self.text])

        # SuperEntity([self.sprites], position = (100, 100))
        # Entity([self.sprites], position = (200, 200))
        # Entity([self.sprites], position = (200, 200), image=card_texture)


        
        # for i in range(2):
        #     suit  = player_hand[i].get_suit()
        #     rank = player_hand[i].get_rank()
        #     texture_name = (suit + rank + '.png')
        #     card_texture = pygame.image.load('textures/' + texture_name).convert_alpha()
        #     card_texture = pygame.transform.scale(card_texture, (100, 100))
        #     Entity([self.sprites], position = (((i * 0.5) + 1) * 100, 600 + (100 * (0.1 * i))), image=card_texture)
        #     # Entity([self.sprites], position = (((i * 0.5) + 1) * 100, 100), image=card_texture)
        #     # Entity([self.sprites], position = (((i * 0.5) + 1) * 100, (i + 1) * 100), image=card_texture)

        # print(f'Players card: {player_hand[0]}, {player_hand[1]}')

        # Entity([self.sprites], position = (50, 300), image=hit_button_texture)
        # Entity([self.sprites], position = (300, 300), image=stand_button_texture)
        # Entity([self.sprites], position = (550, 300), image=double_double_button_texture)
        
        # NOTE: 50 Pixel margins as each texture is 200 pixels wide on an 800 pixel screen.

        # Entity([self.start_buttons], position = (50, 300), image=hit_button_texture)
        # Entity([self.start_buttons], position = (300, 300), image=stand_button_texture)
        # Entity([self.start_buttons], position = (550, 300), image=double_double_button_texture)
        
        # Entity([self.sprites], position = (150, 300), image=hit_button_inverted_texture)
        # Entity([self.sprites], position = (450, 300), image=stand_button_texture)

        # TextEntity([self.text], screen, position, font, text)
        # TextEntity([self.text], self.app.screen, position, font, text)

        self.sprites = pygame.sprite.Group()
        self.start_buttons = pygame.sprite.Group()
        self.game_buttons = pygame.sprite.Group()
        self.text = pygame.sprite.Group()
        
        self.player_hand = []
        self.dealer_hand = []
        self.start_game()

        # self.start_buttons



        Entity([self.start_buttons], position = (50, 300), image=hit_button_texture)
        Entity([self.start_buttons], position = (300, 300), image=stand_button_texture)
        Entity([self.start_buttons], position = (550, 300), image=double_double_button_texture)
        
        Entity([self.game_buttons], position = (150, 300), image=hit_button_inverted_texture)
        Entity([self.game_buttons], position = (450, 300), image=stand_button_texture)
        
    def start_game(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.reset_deck()
        self.deck.shuffle()

        # Deal inital cards
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

        self.update_card_display('GAME_START')

    def update_card_display(self, game_state):
        self.sprites.empty()
        
        for i, card in enumerate(self.player.hand):
            texture_name = f'textures/{card.get_suit()}{card.get_rank()}.png'
            card_texture = pygame.image.load(texture_name).convert_alpha()
            card_texture = pygame.transform.scale(card_texture, (100, 100))
            Entity([self.sprites], position=(100 + i * 120, 600), image=card_texture)

        for i, card in enumerate(self.dealer.hand):
            if i == 1 and (game_state == 'GAME' or game_state == 'GAME_START'):
                texture_name = 'textures/FaceDown.png'
                card_texture = pygame.image.load(texture_name).convert_alpha()
                card_texture = pygame.transform.scale(card_texture, (100, 100))
            else:
                texture_name = f'textures/{card.get_suit()}{card.get_rank()}.png'
                card_texture = pygame.image.load(texture_name).convert_alpha()
                card_texture = pygame.transform.scale(card_texture, (100, 100))
            Entity([self.sprites], position=(100 + i * 120, 200), image=card_texture)

    def hit(self):
        self.player.add_card(self.deck.deal())
        self.update_card_display('GAME')
        if self.player.calculate_hand() > 21:
            self.update_card_display('GAME_OVER')
            return 'GAME_OVER'
        else:
            return 'GAME'
        
    def stand(self):
        while self.dealer.calculate_hand() <= 16:
            self.dealer.add_card(self.deck.deal())
            self.update_card_display('GAME_OVER')
        self.update_card_display('GAME_OVER')
        return 'GAME_OVER'

    def double_down(self):
        self.player.add_card(self.deck.deal())
        self.update_card_display()
        self.stand()


    def update(self):
        pass
        #self.entity.rect.x += 1
        #self.sprites.update()
        #self.update_card_display()


    def draw(self, game_state):
        #self.app.screen.fill('white')
        self.app.screen.fill('#de283a')
        match game_state:
            case 'GAME_START':
                # pass
                self.start_buttons.draw(self.app.screen)
                self.sprites.draw(self.app.screen)
            case 'GAME':
                self.sprites.draw(self.app.screen)
                self.game_buttons.draw(self.app.screen)
            case 'GAME_OVER':
                self.sprites.draw(self.app.screen)
        
    #     self.text.blit_text(self.app.screen, position = (20, 20), font = pygame.font.SysFont('Arial', 16), color = pygame.Color('#38cff5'), text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
    #    "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
    #    "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
    #    "text will disappear underneath the surface")


    def button_press(self, button_type, game_state):
        match button_type:
            case 'hit':
                # print('hit')
                game_state = self.hit()
                # return 'GAME'
            case 'stand':
                # print('stand')
                game_state = self.stand()
                # return 'GAME'
            case 'double down':
                # print('double down')
                game_state = self.double_down()
                # return 'GAME'
        
        return game_state
    


# def get_player_choice():
#     print('Would you like to Hit (H), Stand (S), Double Down (D)?')
#     return input('Player, what would you like to do: ').strip().upper()

# def execute_player_turn(player: Player, deck: Deck, bet_amount: int):
#     player_score = player.calculate_hand()
#     has_hit = False

#     while player_score < 21:
#         player_choice = get_player_choice()
#         if player_choice == 'H':
#             player.add_card(deck.deal())
#             has_hit = True
#         elif player_choice == 'D':
#             if has_hit:
#                 print('You cannot double down after hitting.')
#                 continue
#             if (bet_amount * 2) > player.bank:
#                 print('You do not have the funds to double down.')
#                 continue
#             player.add_card(deck.deal())
#             print('You have doubled down and received one more card.')
#             player_score = player.calculate_hand()
#             break
#         elif player_choice == 'S':
#             break
        
#         player_score = player.calculate_hand()
#         print(f'Player score: {player_score}')

#     return player_choice, player_score

# def execute_dealer_turn(dealer: Dealer, deck: Deck):
#     dealer_score = dealer.calculate_hand()
    
#     while dealer_score <= 16:
#         dealer.add_card(deck.deal())
#         dealer_score = dealer.calculate_hand()

#     return dealer_score

# def place_player_bet(bank_balance):
#     while True:
#         try:
#             bet_amount = int(input('Player, place your bet: '))
#             if 0 < bet_amount <= bank_balance:
#                 return bet_amount
#             print('Invalid bet. Enter a new betting amount: ')
#         except ValueError:
#             print('Invalid input. Please enter a number.')

# def play_blackjack(player: Player, dealer: Dealer, deck: Deck):
#     bet_amount = place_player_bet(player.bank)

#     # Drawing Cards
#     for _ in range(2):
#         player.add_card(deck.deal())
#         dealer.add_card(deck.deal())

#     print(f"Player's score: {player.calculate_hand()}")
#     print(f"Dealer's card: {dealer.hand[0]}")

#     if player.calculate_hand() == 21:
#         print('You hit a blackjack!')
#         player.bank += (1.5 * bet_amount)
#     else:
#         player_choice, player_score = execute_player_turn(player, deck, bet_amount)

#         if player_score > 21:
#             print('You went over 21!')
#             player.bank -= (2 * bet_amount) if player_choice == 'D' else bet_amount
#         else:
#             dealer_score = execute_dealer_turn(dealer, deck)

#             if player_score > dealer_score or dealer_score > 21:
#                 print(f'You win! player: {player_score}, dealer: {dealer_score}')
#                 player.bank += (2 * bet_amount) if player_choice == 'D' else bet_amount
#             elif dealer_score > player_score:
#                 print(f'Dealer won! dealer: {dealer_score}, player: {player_score}')
#                 player.bank -= (2 * bet_amount) if player_choice == 'D' else bet_amount
#             else:
#                 print('You tied!')

#     print(f'New balance: {player.bank}')

# def main():
#     deck = Deck()
#     dealer = Dealer(deck)
#     player = Player(deck)
#     bank_amount = player.bank
#     print(f'You start with: {bank_amount} dollars')
    
#     while bank_amount > 0:
#         player.reset_hand()
#         dealer.reset_hand()
#         deck.reset_deck()
#         deck.shuffle()
#         play_blackjack(player, dealer, deck)
#         bank_amount = player.bank

# if __name__ == "__main__":
#     main()

