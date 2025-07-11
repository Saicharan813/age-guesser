import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 480, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Old School Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_img = pygame.Surface((50, 30))
player_img.fill(WHITE)
player_rect = player_img.get_rect()
player_rect.midbottom = (WIDTH // 2, HEIGHT - 10)
player_speed = 5

# Bullet settings
bullet_img = pygame.Surface((5, 10))
bullet_img.fill(WHITE)
bullets = []

# Enemy settings
enemy_img = pygame.Surface((40, 30))
enemy_img.fill((255, 0, 0))
enemies = []
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 1000)

clock = pygame.time.Clock()
running = True

def move_player(keys, rect):
    if keys[pygame.K_LEFT] and rect.left > 0:
        rect.x -= player_speed
    if keys[pygame.K_RIGHT] and rect.right < WIDTH:
        rect.x += player_speed

def shoot(rect):
    bullet_rect = bullet_img.get_rect()
    bullet_rect.midbottom = rect.midtop
    bullets.append(bullet_rect)

def move_bullets():
    for bullet in bullets[:]:
        bullet.y -= 7
        if bullet.bottom < 0:
            bullets.remove(bullet)

def spawn_enemy():
    enemy_rect = enemy_img.get_rect()
    enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)
    enemy_rect.y = 0
    enemies.append(enemy_rect)

def move_enemies():
    for enemy in enemies[:]:
        enemy.y += 3
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

def check_collisions():
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                break

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ENEMY_SPAWN_EVENT:
            spawn_enemy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot(player_rect)

    keys = pygame.key.get_pressed()
    move_player(keys, player_rect)
    move_bullets()
    move_enemies()
    check_collisions()

    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    pygame.display.flip()

pygame.quit()