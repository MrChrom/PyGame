# import the pygame module
import pygame
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 128, 0))
        self.rect = self.surf.get_rect()
        all_sprites.add(self)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        self.Speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# initialize pygame
pygame.init()

# create the screen object
screen = pygame.display.set_mode((800, 600))

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


# instantiate our player; right now he's just a rectangle
player = Player()

# Variable to keep our main loop running
running = True

enemy = Enemy()

#ADDENEMY = pygame.USEREVENT + 1
#pygame.time.set_timer(ADDENEMY, 250)

# Our main loop!
while running:
    # check for events
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        #elif(event.type == ADDENEMY):
            #new_enemy = Enemy()
            #enemies.add(new_enemy)
            #all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # start drawing
    # blank the screen first
    screen.fill((0, 0, 0))

    # Draw the player to the screen
    # screen.blit(player.surf, player.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display
    pygame.display.flip()