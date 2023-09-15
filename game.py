import pygame
from settings import *
from sprite import *


class Game:
    def __init__(self, player: Snake):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.running = True
        self.background = pygame.image.load("images/backgroung100.png")
        self.call_down = 0
        self.apples_sprites = pygame.sprite.Group()

    def new(self):
        # start a new game
        self.create_apples()
        self.all_sprites.add(self.player)
        self.run()


    def run(self):
        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        eaten_apples = pygame.sprite.spritecollide(self.player, self.apples_sprites, True)
        if eaten_apples:
            self.create_apples()
            self.player.add_tail()
        if self.player.rect.x == 0 or self.player.rect.x == WIDTH - self.player.rect.width:
            self.running = False
        if self.player.rect.y == 0 or self.player.rect.y == HEIGHT - self.player.rect.height:
            self.running = False
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.running = False
                print(self.player.apples_counter)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.change_direction("RIGHT")
                elif event.key == pygame.K_LEFT:
                    self.player.change_direction("LEFT")

                elif event.key == pygame.K_DOWN:
                    self.player.change_direction("DOWN")

                elif event.key == pygame.K_UP:
                    self.player.change_direction("UP")


    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.player.tail_group.draw(self.screen)
        # *after* drawing everything, flip the display
        self.apples_sprites.draw(self.screen)
        pygame.display.flip()

    def create_apples(self):
        apple = Apple()
        self.apples_sprites.add(apple)

    def show_start_screen(self):
        image = pygame.image.load('images/first_screen.png')
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        self.wait_for_key()

    def show_end_screen(self):
        image = pygame.image.load('images/2627196.png')
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        self.running = False
        self.wait_for_key()

    def wait_for_key(self):
        a = True
        while a:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    a = False
                if event.type == pygame.QUIT:
                    a = False
                    self.running = False


player = Snake()
g = Game(player)
g.show_start_screen()
while g.running:
    g.new()
    g.show_end_screen()

pygame.quit()
