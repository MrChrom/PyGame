# import the pygame module
import pygame
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('ref/jet.png').convert()
        print(self.image)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        print(self.image)
        self.rect = self.image.get_rect()
        print(self.image.get_rect())
        print(self.rect)
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

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800: # elif?
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600: # elif?
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('ref/missile.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if pygame.sprite.spritecollideany(self, bullets):
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('ref/cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('ref/bullet.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(midleft=player.rect.center)

    def update(self):
        self.rect.move_ip(7, 0)
        if self.rect.right > 800:
            self.kill()


# initialize pygame
pygame.init()

# create the screen object
screen = pygame.display.set_mode((800, 600))

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Create a custom event for adding a new cloud.
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


# instantiate our player; right now he's just a rectangle
player = Player()
enemy = Enemy()

# Variable to keep our main loop running
running = True


# Our main loop!
while running:

    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    if pressed_keys[K_SPACE]:
        new_bullet = Bullet()
        all_sprites.add(new_bullet)
        bullets.add(new_bullet)

    enemies.update()
    clouds.update()
    bullets.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    #if pygame.sprite.spritecollideany(player, enemies):
        #player.kill()

    pygame.display.flip()

    # This is a test