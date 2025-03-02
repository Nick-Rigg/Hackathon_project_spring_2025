import pygame
import sys
from globals import *
from scene import Scene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock() # Possibly could be removed

        self.running = True

        self.scene = Scene(self)

        self.state = 'GAME_START'     # Game Start - Game - Game Over


    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():

            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                self.running = False
            
            match self.state:
                case 'GAME_START':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 50 <= mouse_position[0] <= 250 and 300 <= mouse_position[1] <= 500:
                            self.state = self.scene.button_press('hit', self.state)
                        elif 300 <= mouse_position[0] <= 500 and 300 <= mouse_position[1] <= 500:
                            self.state = self.scene.button_press('stand', self.state)
                        elif 550 <= mouse_position[0] <= 750 and 300 <= mouse_position[1] <= 500:
                            self.state = self.scene.button_press('double down', self.state)
                case 'GAME':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 150 <= mouse_position[0] <= 350 and 300 <= mouse_position[1] <= 500:
                            self.state = self.scene.button_press('hit', self.state)
                        elif 450 <= mouse_position[0] <= 650 and 300 <= mouse_position[1] <= 500:
                            self.state = self.scene.button_press('stand', self.state)
                case 'GAME_OVER':
                    pass

        # self.scene.update(self, self.state)
        # self.scene.update(self.state)
        # self.scene.update(self)
        self.scene.update()

        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):
        #self.screen.fill('white')
        self.scene.draw(self.state)
    
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()