# John Lorenz IV // First pygame program
# .. a cat in space with a cool jetpack?
import pygame, sys
import random
import player as p
import asteroids as a
import menu as m
import background as b

WINDOW_HEIGHT = 1920
WINDOW_WIDTH = 1080
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
RED = (255, 0 , 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

SPRITE_OFFSET = 90


def generateRandomLocations(): # random locations for platforms
    rX = []
    rY = []
    for x in range(0, 50):
        rX.append(random.randint(0, WINDOW_HEIGHT))
        rY.append(random.randint(0, WINDOW_WIDTH))
    return rX, rY

def drawPlatforms(screen, rX, rY): # draws the platforms, given random x and y
    xPos = 200
    yPos = 100
    platformLength = 100
    platformHeight = 20
    i = 0
    smallPlatformLength = 40
    while xPos < 1920 and yPos < 1080:
        rectanglePlatform = pygame.Rect(xPos, yPos, platformLength, platformHeight)
        shortRectanglePlatform = pygame.Rect(rX[i], rY[i], smallPlatformLength, platformHeight)
        pygame.draw.rect(screen, RED, rectanglePlatform)
        pygame.draw.rect(screen, YELLOW, shortRectanglePlatform)
        xPos += 200
        yPos += 100
        i += 1

def drawSpace(background, screen):
    screen.blit(background, (0,0))

def shootingStars():
    # Emulate shooting star effects
    pass

def runAsteroids(asteroids, screen, dt, objectPos):
    pass

def drawLasers(screen, beam):
    if not beam: # if no lasers were shot, return
        return
    for segment in beam:
        pygame.draw.rect(screen, RED, segment)

def drawKittyUsingOffset(screen, kitty, coords):
    # Centers our cat sprite on its hitbox/player location
    xPos = coords[0]-30
    yPos = coords[1]-45
    screen.blit(kitty, [xPos, yPos])

def main():
    pygame.init()

    FPS = 144
    fpsClock = pygame.time.Clock()

    
    # Screen dimensions -> Make changeable via settings window?
    screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

    # Movement object tracks player position and processes keystrokes
    player = p.player(WINDOW_HEIGHT, WINDOW_WIDTH, SPRITE_OFFSET)
    # Asteroid object
    asteroids = a.asteroids(0, WINDOW_HEIGHT, WINDOW_WIDTH)
    # ESC activated Menu
    menu = m.menu(WINDOW_HEIGHT, WINDOW_WIDTH)
    # Scrolling background
    space = b.space(screen)

    # Title
    pygame.display.set_caption('Ares') 

    # This is our player's image/sprite
    kitty = pygame.image.load('sprites/rocket_cat_sprite.png')

    # Asteroid image
    ast_2 = pygame.image.load('sprites/rough_sprite_asteroid2.png')

    # Background image
    bg = pygame.image.load('backgrounds/rough_background.png')

    RUNNING = True
    PAUSED = False
    dt = fpsClock.tick(FPS)
    while RUNNING:
        events = pygame.event.get()
        

        for event in events:
            if event.type == pygame.QUIT:
                RUNNING = False
         
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            PAUSED = True
        if keys[pygame.K_r]:
            PAUSED = False

        if PAUSED == False:
            # Register Key Movements
            laserData = player.act(keys, dt, asteroids.retrievePosition(), screen)

            # Re-draw each frame
            screen.fill(BLACK)
            #drawSpace(bg, screen)
            space.drawSpace(dt)
            drawLasers(screen, laserData[1])
            drawKittyUsingOffset(screen, kitty, player.retrievePosition())
            player.drawPlayerHitBox(screen)
            # Spawn our Asteroids, and check for collisions, or off-map movement
            asteroids.createAsteroids(screen, dt)
            asteroids.checkAsteroidHealth(asteroids.impacted(player.retrievePosition()), laserData[0])
        else:
            menu.drawMenu(screen)


        dt = fpsClock.tick(FPS) # Game clock
        pygame.display.flip() # refresh screen each cycle
    
    pygame.quit()


if __name__ == "__main__":
    main()