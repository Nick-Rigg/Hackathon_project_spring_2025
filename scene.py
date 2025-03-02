import pygame
from globals import *
from sprite import Entity       #, SuperEntity
from text import TextEntity
from game_functions import *

class Scene:
    def __init__(self, app) -> None:
        self.app = app

        # card_texture = pygame.image.load('textures/Club2.png').convert_alpha()
        # card_texture = pygame.transform.scale(card_texture, (100, 100))
        font = pygame.font.SysFont('Arial', 64)
        screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
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

        

        self.sprites = pygame.sprite.Group()
        self.text = pygame.sprite.Group()
        self.entity = Entity([self.sprites])
        self.text = TextEntity([self.text])
        # SuperEntity([self.sprites], position = (100, 100))
        # Entity([self.sprites], position = (200, 200))
        # Entity([self.sprites], position = (200, 200), image=card_texture)
        TextEntity([self.text], screen, position, font, text)


        for i in range(2):
            suit  = player_hand[i].get_suit()
            rank = player_hand[i].get_rank()
            texture_name = (suit + rank + '.png')
            card_texture = pygame.image.load('textures/' + texture_name).convert_alpha()
            card_texture = pygame.transform.scale(card_texture, (100, 100))
            Entity([self.sprites], position = (((i * 0.5) + 1) * 100, 100 + (100 * (0.1 * i))), image=card_texture)
            # Entity([self.sprites], position = (((i * 0.5) + 1) * 100, 100), image=card_texture)
            # Entity([self.sprites], position = (((i * 0.5) + 1) * 100, (i + 1) * 100), image=card_texture)

        print(f'Players card: {player_hand[0]}, {player_hand[1]}')

        # NOTE: 50 Pixel margins as each texture is 200 pixels wide on an 800 pixl screen.
        Entity([self.sprites], position = (50, 300), image=hit_button_texture)
        Entity([self.sprites], position = (300, 300), image=stand_button_texture)
        Entity([self.sprites], position = (550, 300), image=double_double_button_texture)



    def update(self):
        #pass
        #self.entity.rect.x += 1
        #self.sprites.update()
        pass


    def draw(self, game_state):
        #self.app.screen.fill('white')
        self.app.screen.fill('#de283a')
        match game_state:
            case 'GAME_START':
                pass
                # self.sprites.draw(self.app.screen)
            case 'GAME':
                self.sprites.draw(self.app.screen)
            case 'GAME_OVER':
                self.sprites.draw(self.app.screen)
        
    #     self.text.blit_text(self.app.screen, position = (20, 20), font = pygame.font.SysFont('Arial', 16), color = pygame.Color('#38cff5'), text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
    #    "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
    #    "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
    #    "text will disappear underneath the surface")


    def button_press(self, button_type):
        match button_type:
            case 'hit':
                print('hit')
            case 'stand':
                print('stand')
            case 'double down':
                print('double down')

    

