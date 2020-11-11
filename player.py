import pygame
class player(object):
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, SPRITE_OFFSET):
        self.wh = WINDOW_HEIGHT
        self.ww = WINDOW_WIDTH
        self.SPRITE_OFFSET = SPRITE_OFFSET
        self.playerPos = [int(WINDOW_HEIGHT/2), WINDOW_WIDTH-SPRITE_OFFSET]
        self.LASER_RANGE = 250
        self.LASER_TOLERANCE = 5

# All of our player's actions are handled here.
    def act(self, keys, dt, asteroidPos, screen):
        asteroidHit = False
        beam = []
        if keys[pygame.K_a]:
            self.playerPos[0] -= 1 * dt
        if keys[pygame.K_d]:
            self.playerPos[0] += 1 * dt
        if keys[pygame.K_w]:
            self.playerPos[1] -= 1 * dt
        if keys[pygame.K_s]:
            self.playerPos[1] += 1 * dt
        if keys[pygame.K_SPACE]:
            asteroidHit, beam = self.lasers(screen, asteroidPos)
        
        return [asteroidHit, beam]

    def lasers(self, screen, asteroidPos):
        xPos = self.playerPos[1] + 0
        yPos = self.playerPos[0] + 0
        beam = []
        asteroidHit = False
        for x in range(0,self.LASER_RANGE):
            xPos -= 1
            yPos += 1
            rect = pygame.Rect(yPos, xPos, 2, 2)
            beam.append(rect)
            if asteroidPos[0] != None:
                xDiff = abs(asteroidPos[1] - xPos)
                yDiff = abs(asteroidPos[0] - yPos)
            else:
                xDiff = self.LASER_TOLERANCE+1
                yDiff = self.LASER_TOLERANCE+1
            if xDiff <= self.LASER_TOLERANCE and yDiff <= self.LASER_TOLERANCE:
                asteroidHit = True
            
            # Debugging laser
            tol1 = pygame.Rect(xPos-xDiff, yPos-yDiff, 5, 5)
            tol2 = pygame.Rect(xPos+xDiff, yPos+yDiff, 5, 5)
            pygame.draw.rect(screen, (0, 255, 0), tol1)
            pygame.draw.rect(screen, (0, 255, 0), tol2)
        return asteroidHit, beam

    def drawLasers(self, screen, beam): ## UNUSED, SEE DRAW LASERS IN MAIN
        if not beam: # if no lasers were shot, return
            return
        for segment in beam:
            pygame.draw.rect(screen, (255, 0 ,0), segment)

    def gravity(self, dt):
        if self.playerPos[1] < self.ww-self.SPRITE_OFFSET:
            self.playerPos[1] += 1 * dt

    def retrievePosition(self):
        adjustedPlayerPos = [self.playerPos[0]-self.SPRITE_OFFSET, self.playerPos[1]-self.SPRITE_OFFSET]
        return self.playerPos

    def drawPlayerHitBox(self, screen):
        rect = pygame.Rect(self.playerPos[0], self.playerPos[1], 5, 5)
        pygame.draw.rect(screen, (255, 0, 0), rect)