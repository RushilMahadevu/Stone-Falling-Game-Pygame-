# import libraries
import pygame
import random
import os


# init pygame
pygame.init()

# game window dimensions
SCREEN_WIDTH = 982
SCREEN_HEIGHT = 510

# pos for middles
MIDDLE_WIDTH = SCREEN_WIDTH // 2 - 86
MIDDLE_HEIGHT = SCREEN_HEIGHT // 2

# game vars
bg_scroll = 0
VEL = 7.5
rock_vel = 4
dx = MIDDLE_WIDTH
dy = MIDDLE_HEIGHT
rotate = 0
dy_rock = 30
MAX_ROCKS = 5
score = 0

# load images
bg_image = pygame.image.load('desert.png')
stone_image = pygame.image.load('stone.png')

# function for drawing bg
def draw_bg(bg_scroll):
    screen.blit(bg_image, (0, 0 + bg_scroll))
    screen.blit(bg_image, (0, -600 + bg_scroll))

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('')


rand_width = random.randint(50, SCREEN_WIDTH - 50)
rand_scale_rock = random.randint(50, 90)

# set frame rate
clock = pygame.time.Clock()
FPS = 60


run = True
while run:

    clock.tick(FPS)


    draw_bg(bg_scroll)

    person = pygame.Rect(dx, dy, 250, 250)
    stone_rect = pygame.Rect(rand_width, dy_rock, rand_scale_rock, rand_scale_rock)


    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and person.x - VEL > 0:  # LEFT
        dx -= VEL
        rotate = 5
    if keys_pressed[pygame.K_d] and person.x + VEL < SCREEN_WIDTH - 250:  # RIGHT
        dx += VEL
        rotate = -5


    person_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('person.png'), (250, 250)), rotate)
    stone_image = pygame.transform.scale(pygame.image.load('stone.png'), (rand_scale_rock, rand_scale_rock))

    screen.blit(person_image, (dx, dy))

    screen.blit(stone_image, (rand_width, dy_rock))

    dy_rock += rock_vel
    if dy_rock > 460:
        score += 1
        dy_rock = 0
        rand_width = random.randint(rand_scale_rock, SCREEN_WIDTH - rand_scale_rock)
        rand_scale_rock = random.randint(50, 90)
        screen.blit(stone_image, (rand_width, dy_rock))
        print(score)
        if score >= 5:
            rock_vel = 6
        if score >= 10:
            rock_vel = 8
        if score >= 15:
            rock_vel = 10


    # collision checks
    if pygame.Rect.colliderect(person, stone_rect):
        run = False

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # update display

    pygame.display.update()


pygame.quit()
