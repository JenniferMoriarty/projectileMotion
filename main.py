


import pygame
import math
pygame.init()#initializes Pygame
pygame.display.set_caption("parametric projectile motion")#sets the window title
screen = pygame.display.set_mode((1600, 800))#creates game screen
xpos = 0
ypos = 0
t=0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
pull = False
fly = False
landed = False
gameover = False
clock = pygame.time.Clock() #set up clock
keys = [False]

#gameloop###################################################
while gameover == False:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
#input section----------------------------------------------
        if event.type == pygame.QUIT: #close game window
            break
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_r:
                keys[0]=True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                keys[0]=False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pull = True #pull is the state where you're aiming the balloon

        if event.type == pygame.MOUSEBUTTONUP:
            pull = False
            fly = True #fly is the state where you've let go of the balloon
            releaseX = mousePos[0]
            releaseY = mousePos[1]

        if event.type == pygame.MOUSEMOTION:
             mousePos = event.pos
#physics section------------------------------------------
                     
    if fly is True:
        t+=.1
        ##########equations for projectile motion#######################
        xdist = abs(100-releaseX) #absolute value
        hyp = math.sqrt(xdist*xdist + 60*60) #pythagorean theorem
        print("hyp:", hyp)
        angle = math.acos(xdist/hyp) #arcosine
        print("angle is ", angle*180/math.pi)
        
        #formula for parametric projectile motion
        xpos = hyp*5*math.cos(angle)*t + releaseX
        ypos = -hyp*5*math.sin(angle)*t + (.5*(98.0)*t*t) + releaseY
        
        print("balloon is at", xpos, ypos)
        
    if ypos > 750:
        landed = True #landed is the state where the balloon has hit the ground and isn't moving
        fly = False
        
    if keys[0] == True:
        pull = False
        fly = False
        landed = False
        xpos = 100
        ypos = 700
        t=0
        print("resetting game!")
#render section---------------------------------------------
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    #print("pull:", pull, "fly:", fly, "landed:", landed)
    
    #ground
    pygame.draw.rect(screen, (50, 200, 20), (0, 750, 2000, 50))
 
    #grid lines
    for i in range(20):
        pygame.draw.line(screen, (240, 240, 200), (i*100, 0), (i*100, 800), 1)
    #pole
    pygame.draw.rect(screen, (200, 200, 200), (100,700,10,60))
    
    if pull == False and fly == False and landed == False: #draw at start position
        pygame.draw.circle(screen, (200, 50, 50), (100, 700), 10)
    elif pull == True: #draw at mouse position
        pygame.draw.circle(screen, (200, 50, 50), (mousePos[0], mousePos[1]), 10)
        pygame.draw.line(screen, (100, 100, 100), (100, 700), (mousePos[0], mousePos[1]), 2)
    elif fly == True or landed == True: #draw on ground
        pygame.draw.circle(screen, (200, 50, 50), (xpos, ypos), 10)
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()

