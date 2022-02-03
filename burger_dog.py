from dis import dis
import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog!")


# Set FPS and clock 
FPS = 60
clock = pygame.time.Clock()

# Set game values 
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100

STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.25
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL

burger_velocity = STARTING_BURGER_VELOCITY


# Set colours 
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE=(246,170,54)
RED = (255,0,0)
PURPLE = (150,0,250)

# Set fonts 
font = pygame.font.Font("./burger_dog/assets/WashYourHand.ttf", 32)

# Set text 
points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10,10)

score_text = font.render("Score: " + str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10,50)

title_text = font.render("BURGER DOG", True, RED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, 30)

burgers_eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
burgers_eaten_rect = burgers_eaten_text.get_rect()
burgers_eaten_rect.center = (WINDOW_WIDTH//2, 70)

lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render("Boost: "+str(boost_level), True, PURPLE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render("Final Score: "+str(score), True, ORANGE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# Set sounds and music 
bark_sound = pygame.mixer.Sound("./burger_dog/assets/bark_sound.wav")
miss_sound = pygame.mixer.Sound("./burger_dog/assets/miss_sound.wav")

pygame.mixer.music.load("./burger_dog/assets/bd_background_music.wav")

# Set images
player_image_right = pygame.image.load("./burger_dog/assets/dog_right.png")
player_image_left = pygame.image.load("./burger_dog/assets/dog_left.png")

player_image = player_image_right
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("./burger_dog/assets/burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)


# main game loop
running = True
while running:
    # see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    
    # fill the display
    display_surface.fill(BLACK)

    # blit the HUD
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(burgers_eaten_text, burgers_eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    display_surface.blit(player_image, player_rect)

    pygame.draw.line(display_surface, WHITE, (0,100), (WINDOW_WIDTH,100), 2)

    pygame.display.update()
    clock.tick(FPS)



pygame.quit()