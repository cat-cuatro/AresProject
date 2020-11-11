import pygame, random
class asteroids(object):
    def __init__(self, difficulty, WINDOW_HEIGHT, WINDOW_WIDTH):
        self.sprite = pygame.image.load('sprites/rough_sprite_asteroid2.png')
        self.asteroidList = []
        self.wh = WINDOW_HEIGHT
        self.ww = WINDOW_WIDTH
        self.activeAsteroid = None
        self.activeAsteroidLocation = None
        self.font = None
        self.text = None
        self.tolerance = 50 # Hard coded parameter, can be changed with difficulty (image scaling??)
        self.initializeAsteroids(difficulty)
        self.printList()
        random.seed(0)

    def asteroidCounter(self, screen):
        asteroidCounter = str(len(self.asteroidList))
        self.text = self.font.render("Asteroids Remaining: "+asteroidCounter, True, (0,128,0))
        screen.blit(self.text, (0, 0))

    def initializeAsteroids(self, difficulty):
        numberOfAsteroids = 100
        if difficulty > 0:
            numberOfAsteroids *= difficulty
        
        for x in range(0, numberOfAsteroids):
            randomLocation = self.spawnLocations()
            self.asteroidList.append([self.sprite, randomLocation])

        self.font = pygame.font.SysFont("couriernew", 28)
        self.text = self.font.render("Asteroids", True, (0, 128, 0))

    def spawnLocations(self):
        # Variable spawn locations
        x = self.wh - random.randint(-500, 500)
        offscreenOffset = 100
        
        #x += offscreenOffset
        y = -offscreenOffset
        return [x, y]

    def spawnAsteroid(self):
        # Activate an asteroid from the list
        if self.activeAsteroid == None and self.asteroidList:
            asteroid = self.asteroidList.pop()
            self.activeAsteroid = asteroid[0]
            self.activeAsteroidLocation = asteroid[1]
    
    def drawAsteroid(self, screen):
        # Blit asteroid to screen
        if self.activeAsteroid == None:
            return

        screen.blit(self.activeAsteroid, [self.activeAsteroidLocation[0]-15, self.activeAsteroidLocation[1]-15])
        self.drawHitBox(screen)

    def moveAsteroid(self, dt):
        # Asteroids move diagonally 1 pixel at a time
        if self.activeAsteroid == None:
            return

        self.activeAsteroidLocation[0] -= 1 * dt/2
        self.activeAsteroidLocation[1] += 1 * dt/2
        #print(self.activeAsteroidLocation)

    def checkAsteroidHealth(self, impacted, lasered):
        # When asteroids leave the screen, destroy them
        offscreenOffset = 40
        if self.activeAsteroid == None:
            return
        
        if self.activeAsteroidLocation[0] < 0 or self.activeAsteroidLocation[1] == self.ww:
            self.activeAsteroid = None
            self.activeAsteroidLocation = []
        elif impacted == True or lasered == True:
            self.activeAsteroid = None
            self.activeAsteroidLocation = []

    def createAsteroids(self, screen, dt):
        # Pops remaining asteroids from asteroid list
        self.spawnAsteroid()
        # Moves asteroids diagonally
        self.moveAsteroid(dt)
        # Draws asteroids to the screen
        self.drawAsteroid(screen)
        # Displays the number of asteroids remaining
        self.asteroidCounter(screen)
        # Destroys asteroids that leave the screen space
        #self.destroyAsteroid()

    def printList(self):
        #print(self.asteroidList)
        pass

    def impacted(self, objectLocation, screen=None):
        if self.activeAsteroid == None: 
            return
        impacted = False
        objectXPos = objectLocation[0]
        objectYPos = objectLocation[1]
        asteroidXPos = self.activeAsteroidLocation[0]
        asteroidYPos = self.activeAsteroidLocation[1]
        tolerance = self.tolerance
        xDiff = abs(objectXPos - asteroidXPos)
        yDiff = abs(objectYPos - asteroidYPos)
        if xDiff <= tolerance and yDiff <= tolerance:
            impacted = True
            print('Impacted! Comet:', len(self.asteroidList))

        if screen != None: # Draw tolerance box
            tol1 = pygame.Rect(asteroidXPos-xDiff, asteroidYPos-yDiff, 5, 5)
            tol2 = pygame.Rect(asteroidXPos+xDiff, asteroidYPos+yDiff, 5, 5)
            pygame.draw.rect(screen, (0, 255, 0), tol1)
            pygame.draw.rect(screen, (0, 255, 0), tol2)
            

        return impacted

    def retrievePosition(self):
        if not self.activeAsteroidLocation:
            location = [None, None]
        else:
            location = self.activeAsteroidLocation
        return location

    def drawHitBox(self, screen):
        rect = pygame.Rect(self.activeAsteroidLocation[0], self.activeAsteroidLocation[1], 5, 5)
        pygame.draw.rect(screen, (255, 0 ,0), rect)