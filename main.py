# creating a new pygame game called pong

import random
import pygame 
import sys

# general setup

pygame.init()
clock = pygame.time.Clock()

# creating the screen
screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# main variables

RUN = True
FPS = 60

# game objects

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# game logic variables

ball_speed_x = 7
ball_speed_y = 7

player_speed = 0


difficulty = random.choice((3, 4,  5 , 6 , 5 , 7, 8 , 5 , 7 , 8 , 5 , 9 , 10 ,12 ,11, 13, 15))


# game logic functions

def ball_animation():
    global ball_speed_x, ball_speed_y
    
    # ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # ball collision with walls
    
    global player_score, opponent_score,score_timer
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        
    if ball.left <= 0:
        player_score += 1
        # ball_restart()
        score_timer = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opponent_score += 1
        # ball_restart()
        score_timer = pygame.time.get_ticks()
        
    # ball collision with player
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1.5
        ball_speed_x = int(ball_speed_x)
def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height 
     
def ball_restart():
    global ball_speed_x, ball_speed_y,score_timer
    
    current_time = pygame.time.get_ticks()
    if current_time - score_timer < 700: 
        number_tree = game_font.render(str(3), True, (255, 255, 255))
        screen.blit(number_tree, (screen_width/2 - 10, screen_height/2 + 20))
    if 700 < current_time - score_timer < 1400: 
        number_two = game_font.render(str(2), True, (255, 255, 255))
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
    if 1400 < current_time - score_timer < 2100: 
        number_one = game_font.render(str(1), True, (255, 255, 255))
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))
        
    if current_time - score_timer < 2100:
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x , ball_speed_y = 0, 0
    else:
        ball_speed_x = 2
        ball_speed_y = 2
        ball.center = (screen_width/2, screen_height/2)
    
        ball_speed_y *= random.choice((1, -1))
        ball_speed_x *= random.choice((1, -1))

        score_timer = None
def opponent_ai():
    run = random.choice((True, False , True , True))
    if run :
        if opponent.top < ball.y:
            opponent.top += difficulty
        if opponent.top > ball.y:
            opponent.top -= difficulty
            
# game text 
# score
player_score = 0
opponent_score = 0
# creating font
game_font = pygame.font.Font("freesansbold.ttf", 32)

# score timer
score_timer = True

while RUN:
    
    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                FPS = 30
            if event.key == pygame.K_UP :
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                FPS = 60
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
    

    
           
    # ball animation
    ball_animation()
    # player movement
    player.y += player_speed
    player_animation()
    # opponent movement
    opponent_ai() # opponent movement   
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    # fill screen with black
    screen.fill((0,0,0))
    # draw text
    player_text = game_font.render(f"{player_score}", True, (255,255,255))
    screen.blit(player_text, (660,470))
    opponent_text = game_font.render(f"{opponent_score}", True, (255,255,255))
    screen.blit(opponent_text, (600,470))
    # draw objects
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), opponent)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width/2, 0), (screen_width/2, screen_height))

    if score_timer is not None:
        ball_restart()
        
    # updating the screen
    pygame.display.flip()
    clock.tick(FPS)
    
