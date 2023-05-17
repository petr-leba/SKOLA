import pygame
import random
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooter Game")
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("player.png").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()
bullet_image = pygame.image.load("bullet.png").convert_alpha()
powerup_image = pygame.image.load("powerup.png").convert_alpha()

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.speed = 5
        self.health = 100
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        bullet = Bullet(self.rect.right, self.rect.centery)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = random.randint(0, height - self.rect.height)
        self.speed = random.randint(2, 6)
        self.health = 20

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > width:
            self.kill()

class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = powerup_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, width - 50)
        self.rect.y = random.randint(50, height - 50)

    def update(self):
        pass

# Initialize game objects
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Spawn enemies
    if random.randint(0, 30) == 0:
        enemy = Enemy()
        enemies.add(enemy)

    # Spawn power-ups
    if random.randint(0, 500) == 0:
        powerup = Powerup()
        powerups.add(powerup)

    # Update game objects
    player.update()
    enemies.update()
    bullets.update()
    powerups.update()

    # Check for collisions
    player_hit_enemies = pygame.sprite.spritecollide(player, enemies, True)
    for enemy
