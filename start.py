import sys
import pygame

WIDTH = 600
HEIGHT = 800
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BG_COLOR = BLACK

class Game():
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Разрешение экрана
        pygame.display.set_caption("TableStars")
        self.clock = pygame.time.Clock()
        self.screen.fill(BG_COLOR)
        pygame.mixer.init() #Звук
        self.ship = pygame.image.load('images/ship.png')
        self.ship = pygame.transform.scale(self.ship, (WIDTH*0.16,WIDTH*0.16))
        self.ship_rect = self.ship.get_rect(bottomright=(WIDTH/2+(WIDTH*0.16)/2, HEIGHT*0.9))
        self.screen.blit(self.ship, self.ship_rect)



    def run_game(self):
        while True:
            for event in pygame.event.get():
                self.screen.fill(BG_COLOR)
                if event.type == pygame.QUIT:
                    sys.exit()
                self.x, self.y = pygame.mouse.get_pos()
                self.ship_rect = self.ship.get_rect(bottomright=(self.x+(WIDTH*0.16)/2, HEIGHT*0.9))
                self.screen.blit(self.ship, self.ship_rect)
                # self.screen.fill(BG_COLOR)




            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()



