import pygame
import random



        
pygame.init()
pygame.font.init() 
font = pygame.font.SysFont('CenturyGothicRegular', 50)


clock = pygame.time.Clock()

WIDHT = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Pong")

#Components
ball = pygame.Rect(WIDHT/2 - 15, HEIGHT/2 - 15, 30,30)
player = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)
opponent = pygame.Rect(WIDHT - 25, HEIGHT/2 - 70, 10, 140)

light_grey = (220,220,220)



ballspeed_x = 5 * random.choice((1,-1))
ballspeed_y = 5 * random.choice((1,-1))


speed = 7
playerspeed = 0
opponentspeed = 0

player_score = 0
opponent_score = 0


def update_scores():
    text = f"{str(player_score)} {str(opponent_score)}"
    txt = font.render(text, True, light_grey)
    txt_rect = txt.get_rect(center=(WIDHT/2, HEIGHT/2))
    screen.blit(txt, txt_rect)
    
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
        if event.type == pygame.KEYDOWN:
            #Player
            if event.key == pygame.K_DOWN:
                playerspeed += speed
            if event.key == pygame.K_UP:
                playerspeed -= speed
            
            #Opponent
            if event.key == pygame.K_s:
                opponentspeed += speed
            if event.key == pygame.K_w:
                opponentspeed -= speed
            
        if event.type == pygame.KEYUP:
            #Player
            if event.key == pygame.K_DOWN:
                playerspeed -= speed
            if event.key == pygame.K_UP:
                playerspeed += speed
            
            #Opponent
            if event.key == pygame.K_s:
                opponentspeed -= speed
            if event.key == pygame.K_w:
                opponentspeed += speed
            
            
    player.y += playerspeed
    opponent.y += opponentspeed
    
    if player.top <= 0:
        	player.top = 0
    if player.bottom >= HEIGHT:
        	player.bottom = HEIGHT
  
    if opponent.top <= 0:
        	opponent.top = 0
    if opponent.bottom >= HEIGHT:
    	opponent.bottom = HEIGHT
     
    
    ball.x += ballspeed_x
    ball.y += ballspeed_y
    
    
    
    #Wall collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballspeed_y *= -1
        
    if ball.left <= 0:
        #Opponent wins!
        opponent_score += 1
        # Reset the ball
        ballspeed_x *= random.choice((1,-1))
        ball.center = (WIDHT/2, HEIGHT/2)
        
    if ball.right >= WIDHT:
        #Player wins!
        player_score += 1
        
        
        # Reset the ball
        ballspeed_x *= random.choice((1,-1))
        ball.center = (WIDHT/2, HEIGHT/2)
        
        
        

    #Player collision
    if player.colliderect(ball):
        ball.x = player.right
        ballspeed_x *= -1

   
   
    if opponent.colliderect(ball):
        ball.x = 750
        
        ballspeed_x *= -1

    screen.fill((0,0,0))
    pygame.draw.rect(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.line(screen, light_grey, (WIDHT/2, 0),(WIDHT/2,HEIGHT), 1)
    update_scores()
    
    pygame.display.flip()
    clock.tick(FPS)
