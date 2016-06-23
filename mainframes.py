#Asteroid Field.
#A minigame where you avoid falling asteroids.
#Copyright (C) 2016 Corinna Yong

import pygame, sys, time, random, math
from pygame.locals import *

pygame.init()

#Here we're going to set up the refresh rate, giving out game a max fps, so it doesn't run too often.
FPS = 50
clock = pygame.time.Clock()

display_width = 800 #x
display_height = 600 #y
SHIP_SPEED = 15
ASTEROID_SPEED = 7.0
BESTTIME = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pywindow = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Asteroid Field')

###MUSIC
music = pygame.mixer.music.load("One Curious Nightfall - Industrial Melancholy.mp3")
pygame.mixer.music.play(-3)
pygame.mixer.music.set_volume(0.5)

#GRAPHICS, IMAGES, SOUNDS
ship = 'Ships.png'
asteroid = 'csasteroid.png'
backgroundImg = 'csbackground.png'
logo = 'cslogo.png'
icon = pygame.image.load('cslogo.png').convert_alpha() #NEW ICON LATER!
icon = pygame.display.set_icon(icon)

#IMPORT ITEMS
ship = pygame.image.load(ship).convert_alpha() #Just setting the starting point for our image.
asteroid1 = pygame.image.load(asteroid).convert_alpha()
asteroid2 = pygame.image.load(asteroid).convert_alpha()
asteroid3 = pygame.image.load(asteroid).convert_alpha()
asteroid4 = pygame.image.load(asteroid).convert_alpha()
asteroid5 = pygame.image.load(asteroid).convert_alpha()
asteroid6 = pygame.image.load(asteroid).convert_alpha()
asteroid7 = pygame.image.load(asteroid).convert_alpha()
asteroid8 = pygame.image.load(asteroid).convert_alpha()
asteroid9 = pygame.image.load(asteroid).convert_alpha()
asteroid10 = pygame.image.load(asteroid).convert_alpha()
background = pygame.image.load(backgroundImg).convert()
background = pygame.transform.scale(background, (display_width, display_height))
logo = pygame.image.load(logo).convert_alpha()

smallfont = pygame.font.Font('ARCADECLASSIC.TTF', 25)
medfont = pygame.font.Font('ARCADECLASSIC.TTF', 30)
largefont = pygame.font.Font('ARCADECLASSIC.TTF', 80)

def game_intro():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        pywindow.blit(background, (0,0))
        pywindow.blit(logo, ((display_width/4), (display_height/4)))

        message_to_screen('Avoid the falling asteroids', WHITE, 50)
        message_to_screen('using your left and right arrow keys', WHITE, 100)
        message_to_screen('press SPACE to play or ESCAPE to quit', WHITE, 150)
        
        pygame.display.update()
##        clock.tick(15)

def text_objects(text, color, size):
    if size == 'small':
        textSurface = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurface = medfont.render(text, True, color)
    elif size == 'large':
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size='small'):
    textSurf, textRect = text_objects(msg, color, size) #revamp code below
    textRect.center = (display_width/2), (display_height/2) + y_displace
    pywindow.blit(textSurf, textRect)

def gameLoop():
    global ASTEROID_SPEED
    global BESTTIME
    gameExit = False
    gameOver = False

    shipX = display_width / 2
    shipXchange = 0
    shipY = display_height - 100
    backgroundX = 0
    backgroundY = 0
    asteroidX1 = random.randrange(0, display_width)
    asteroidX2 = random.randrange(0, display_width)
    asteroidX3 = random.randrange(0, display_width)
    asteroidX4 = random.randrange(0, display_width)
    asteroidX5 = random.randrange(0, display_width)
    asteroidX6 = random.randrange(0, display_width)
    asteroidX7 = random.randrange(0, display_width)
    asteroidX8 = random.randrange(0, display_width)
    asteroidX9 = random.randrange(0, display_width)
    asteroidX10 = random.randrange(0, display_width)
    asteroidY = -75
    TIMER = 0
    timerText = medfont.render('TIME ' + str(TIMER), 2, WHITE)
    timerrect = timerText.get_rect()
    timerX = (display_width - timerrect[2]) / 2
 
    while not gameExit: #CHECK FOR EVENT HANDLING
##        print(ASTEROID_SPEED) #CHECK/TEST

        if gameOver == True:
            ASTEROID_SPEED = 7.0
            if(int(displaytimer) > BESTTIME):
                BESTTIME = int(displaytimer)
                
        while gameOver == True:
            
            pywindow.blit(background, (0,0))
            message_to_screen('Game Over', WHITE, y_displace = -100, size = 'large')
            message_to_screen('TIME ' + str(displaytimer), WHITE, y_displace= -25, size = 'large')
            message_to_screen('HI TIME ' + str(BESTTIME), WHITE, y_displace = 50, size = 'large')
            message_to_screen('Press the SPACEBAR to play again or ESCAPE to quit', WHITE, y_displace = 100, size = 'medium')
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        return #gameLoop()
                    

        clock.tick(30)
        #COLLISION CHECK
        ship_rect = ship.get_rect(center=(shipX, shipY))
        asteroid_rect1 = asteroid1.get_rect(center=(asteroidX1, asteroidY))
        asteroid_rect2 = asteroid2.get_rect(center=(asteroidX2, asteroidY))
        asteroid_rect3 = asteroid3.get_rect(center=(asteroidX3, asteroidY))
        asteroid_rect4 = asteroid4.get_rect(center=(asteroidX4, asteroidY))
        asteroid_rect5 = asteroid5.get_rect(center=(asteroidX5, asteroidY))
        asteroid_rect6 = asteroid6.get_rect(center=(asteroidX6, asteroidY))
        asteroid_rect7 = asteroid7.get_rect(center=(asteroidX7, asteroidY))
        asteroid_rect8 = asteroid8.get_rect(center=(asteroidX8, asteroidY))
        asteroid_rect9 = asteroid9.get_rect(center=(asteroidX9, asteroidY))
        asteroid_rect10 = asteroid10.get_rect(center=(asteroidX10, asteroidY))
        if ship_rect.colliderect(asteroid_rect1) or ship_rect.colliderect(asteroid_rect2) or ship_rect.colliderect(asteroid_rect3) or ship_rect.colliderect(asteroid_rect4) or ship_rect.colliderect(asteroid_rect5) or ship_rect.colliderect(asteroid_rect6) or ship_rect.colliderect(asteroid_rect7) or ship_rect.colliderect(asteroid_rect8) or ship_rect.colliderect(asteroid_rect9) or ship_rect.colliderect(asteroid_rect10):
            gameOver = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    shipXchange = SHIP_SPEED
                elif event.key == pygame.K_LEFT:
                    shipXchange = -SHIP_SPEED
            elif event.type == KEYUP:
                if event.key == pygame.K_RIGHT:
                    shipXchange = 0
                elif event.key == pygame.K_LEFT:
                    shipXchange = 0

        shipX += shipXchange

        if shipX > display_width: #Allow user to move through the screen (no boundary)
            shipX = 0
        elif shipX < 0:
            shipX = display_width
 
        asteroidY = asteroidY + ASTEROID_SPEED
        if asteroidY > display_height:
            asteroidX1 = random.randrange(0, display_width)
            asteroidX2 = random.randrange(0, display_width)
            asteroidX3 = random.randrange(0, display_width)
            asteroidX4 = random.randrange(0, display_width)
            asteroidX5 = random.randrange(0, display_width)
            asteroidX6 = random.randrange(0, display_width)
            asteroidX7 = random.randrange(0, display_width)
            asteroidX8 = random.randrange(0, display_width)
            asteroidX9 = random.randrange(0, display_width)
            asteroidX10 = random.randrange(0, display_width)
            asteroidY = -25

        pywindow.blit(background, (0,0))
        pywindow.blit(ship, (shipX, shipY))
        pywindow.blit(asteroid1, (asteroidX1, asteroidY))
        pywindow.blit(asteroid2, (asteroidX2, asteroidY))
        pywindow.blit(asteroid3, (asteroidX3, asteroidY))
        pywindow.blit(asteroid4, (asteroidX4, asteroidY))
        pywindow.blit(asteroid5, (asteroidX5, asteroidY))
        pywindow.blit(asteroid6, (asteroidX6, asteroidY))
        pywindow.blit(asteroid7, (asteroidX7, asteroidY))
        pywindow.blit(asteroid8, (asteroidX8, asteroidY))
        pywindow.blit(asteroid9, (asteroidX9, asteroidY))
        pywindow.blit(asteroid10, (asteroidX10, asteroidY))
        
        #TIME UPDATE
        #Timer increment
        seconds = clock.tick() / 15
        TIMER += seconds
        displaytimer = math.trunc(TIMER)
        # Ticks are in milliseconds
        timerText = medfont.render('TIME ' + str(displaytimer), 1, WHITE)
        pywindow.blit(timerText, [timerX,50])
##        print(displaytimer) #TEST
        
        if int(displaytimer) > 0 and int(displaytimer) % 10 == 0: #approx every 10 seconds changes asteroid velocity
            ASTEROID_SPEED += 0.5
        
        pygame.display.update()
        
        clock.tick(FPS) #This refreshes the loop after the FPS rate above
        
    pygame.quit() #Uninitialize
    quit() #Exit game

game_intro()
while True:
    gameLoop()





