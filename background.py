import pygame
from math import sqrt
class space:
    def __init__(self, screen):
        self.bgQuadrant1 = pygame.image.load('backgrounds/rough_background.png')
        self.bgQuadrant2 = pygame.image.load('backgrounds/rough_background.png')
        self.bgQuadrant3 = pygame.image.load('backgrounds/rough_background.png')
        self.bgQuadrant4 = pygame.image.load('backgrounds/rough_background.png')
        self.backgroundPositions = {
            self.bgQuadrant1: [0, 0, (0, 0)],
            self.bgQuadrant2: [0, -1080, (0, -1080)],
            self.bgQuadrant3: [1920, -1080, (1920, -1080)],
            self.bgQuadrant4: [1920, 0, (1920, 0)],
        }
        self.screen = screen
        self.firstPanelEndpoint = [1920, 0]
        self.secondPanelEndpoint = [3840, 0]
    
    def debugLines(self, dt):
        self.firstPanelEndpoint[0] -= 1 * dt/2
        self.firstPanelEndpoint[1] += 1 * dt/2
        self.secondPanelEndpoint[0] -= 1 * dt/2
        self.firstPanelEndpoint[1] += 1 * dt/2

        if self.firstPanelEndpoint[0] <= 0:
            self.firstPanelEndpoint = [1920, 0]
        if self.secondPanelEndpoint[0] <= 0:
            self.secondPanelEndpoint = [3840, 0]

        coords = self.firstPanelEndpoint
        firstBoundRect = pygame.Rect(coords[0], coords[1], 20, 1080)
        coords = self.secondPanelEndpoint
        secondBoundRect = pygame.Rect(coords[0], coords[1], 20, 1080)

        pygame.draw.rect(self.screen, (255, 0, 0), firstBoundRect)
        pygame.draw.rect(self.screen, (0, 255, 255), secondBoundRect)

    def drawSpace(self, dt):
        self.moveBackground(dt)
        '''
        for background in self.backgroundPositions:
            #print(self.backgroundPositions[background])
            self.screen.blit(background, (self.backgroundPositions[background][0], self.backgroundPositions[background][1]))
        '''
        bg = self.bgQuadrant1
        self.screen.blit(bg, (self.backgroundPositions[bg][0], self.backgroundPositions[bg][1]))
        bg = self.bgQuadrant2
        self.screen.blit(bg, (self.backgroundPositions[bg][0], self.backgroundPositions[bg][1]))
        bg = self.bgQuadrant3
        self.screen.blit(bg, (self.backgroundPositions[bg][0], self.backgroundPositions[bg][1]))
        bg = self.bgQuadrant4
        self.screen.blit(bg, (self.backgroundPositions[bg][0], self.backgroundPositions[bg][1]))
        
        #self.debugLines(dt)
    
    def moveBackground(self, dt):
        #print(self.backgroundPositions[self.bgQuadrant1])
        for background in self.backgroundPositions:
            xOrigin = self.backgroundPositions[background][2][0]
            yOrigin = self.backgroundPositions[background][2][1]


            self.backgroundPositions[background][0] -= int(1 * (dt/4))
            self.backgroundPositions[background][1] += int(1 * (dt/4))
            xPos = self.backgroundPositions[background][0]
            yPos = self.backgroundPositions[background][1]

            xDiff = (xPos - xOrigin)**2
            yDiff = (yPos - yOrigin)**2
            distance = sqrt(xDiff+yDiff)
            
            #print(xDiff, yDiff)
            if distance >= 2202:
                self.backgroundPositions[background][0] = xOrigin
                self.backgroundPositions[background][1] = yOrigin