import pygame
import sys
import random


# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up the window
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Demon Killer', True, (255, 0, 0))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/2))
    screen.blit(start_button, (WIDTH/2 - start_button.get_width()/2, HEIGHT/2 + start_button.get_height()/2))


def draw_game_over_screen():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Game Over', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/2 - title.get_height()/3))
    screen.blit(restart_button, (WIDTH/2 - restart_button.get_width()/2, HEIGHT/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (WIDTH/2 - quit_button.get_width()/2, HEIGHT/2 + quit_button.get_height()/2))


# Set up the score counter
score = 0
score_font = pygame.font.SysFont("comicsansms", 72)
score_text = score_font.render(f"kills: {score}", True, (255, 0, 0))
score_text_rect = score_text.get_rect(center=(WIDTH - 200, 100))

# Load the player and enemy images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy3.jfif")
background_image = pygame.image.load("background.JPG")

# Create the player
player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5
player_rect = player_image.get_rect(center=(player_x, player_y))

# baackground
background_x = WIDTH // 2
background_y = HEIGHT // 2
background_rect = background_image.get_rect(center=(background_x, background_y))

# Create the enemies
enemy_list = []
enemy_speed = 2
enemy_spawn_rate = 350
for i in range(1):
    enemy_x = random.randint(0, WIDTH - enemy_image.get_width())
    enemy_y = random.randint(-500, -enemy_image.get_height())
    enemy_rect = enemy_image.get_rect(center=(enemy_x, enemy_y))
    enemy_list.append(enemy_rect)

# Initialize the bullet rect
bullet_rect = None
bullet_image = pygame.Surface((5, 10))
bullet_image.fill((255, 255, 255))

game_state = "start_menu"

pygame.event.clear()
# Start the game loop
while True:

    keys = pygame.key.get_pressed()

    if game_state == "game":

        screen.fill((0, 0, 0))
        screen.blit(background_image, background_rect)
        screen.blit(player_image, player_rect)

        # Update the player position
        if keys[pygame.K_a] and player_rect.left > 0:
            player_rect.move_ip(-player_speed, 0)
        elif keys[pygame.K_d] and player_rect.right < WIDTH:
            player_rect.move_ip(player_speed, 0)

        # Update the enemies position
        for enemy_rect in enemy_list:
            if enemy_rect.top > HEIGHT:
                enemy_list.remove(enemy_rect)
            else:
                enemy_rect.move_ip(0, enemy_speed)

        # Spawn enemies
        if random.randint(0, enemy_spawn_rate) == 0:
            enemy_x = random.randint(0, WIDTH - enemy_image.get_width())
            enemy_y = random.randint(-500, -enemy_image.get_height())
            enemy_rect = enemy_image.get_rect(midbottom=(enemy_x, enemy_y))
            enemy_list.append(enemy_rect)

        # Check for collisions between player and enemies
        if player_rect.collidelist(enemy_list) != -1:
            game_state = "game_over"

        # Handle shooting
        if keys[pygame.K_SPACE]:
            bullet_rect = pygame.Rect(player_rect.centerx, player_rect.top, 5, 10)
            bullet_speed = 10
        if bullet_rect:
            bullet_rect.move_ip(0, -bullet_speed)
            if bullet_rect.bottom < 0:
                bullet_rect = None
            else:
                screen.blit(bullet_image, bullet_rect)
                for enemy_rect in enemy_list:
                    if bullet_rect.colliderect(enemy_rect,):
                        enemy_list.remove(enemy_rect,)
                        bullet_rect = None
                        enemy_spawn_rate -= 2
                        enemy_speed += 0.1
                        score += 1
                        score_font = pygame.font.SysFont("comicsansms", 72)
                        score_text = score_font.render("kills: " + str(score), True, (255, 0, 0))
                        break

        # Check for victory
        if score == 100:
            print("victory")
            print(score, "kills")
            pygame.quit()
            sys.exit()

        for enemy_rect in enemy_list:
            screen.blit(enemy_image, enemy_rect)

        screen.blit(score_text, score_text_rect)

    elif game_state == "start_menu":
        if keys[pygame.K_SPACE]:
            game_state = "game"
        draw_start_menu()

    elif game_state == "game_over":
        if keys[pygame.K_r]:
            game_state = "start_menu"
            score = 0
            enemy_list = []
            enemy_spawn_rate = 350
            for i in range(1):
                enemy_x = random.randint(0, WIDTH - enemy_image.get_width())
                enemy_y = random.randint(-500, -enemy_image.get_height())
                enemy_rect = enemy_image.get_rect(center=(enemy_x, enemy_y))
                enemy_list.append(enemy_rect)

        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

        draw_game_over_screen()

    pygame.display.flip()
    pygame.event.clear()
