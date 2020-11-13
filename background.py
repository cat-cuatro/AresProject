import pygame
from math import sqrt
class space:
    def __init__(self, screen):
        self.centerDiagonalPanel = pygame.image.load('backgrounds/rough_background_square.png')
        self.centerDiagonalPanel2 = pygame.image.load('backgrounds/rough_background_square.png')
        self.upperDiagonalPanel = pygame.image.load('backgrounds/rough_background_square.png')
        self.upperDiagonalPanel2= pygame.image.load('backgrounds/rough_background_square.png')
        self.lowerDiagonalPanel = pygame.image.load('backgrounds/rough_background_square.png')
        self.lowerDiagonalPanel2= pygame.image.load('backgrounds/rough_background_square.png')
        self.backgroundPositions = {
            self.centerDiagonalPanel: [0, 0, (0, 0)],
            self.upperDiagonalPanel: [0, -1920, (0, -1920)],
            self.upperDiagonalPanel2: [1920, -3840, (1920, -3840)],
            self.centerDiagonalPanel2: [1920, -1920, (1920, -1920)],
            self.lowerDiagonalPanel: [1920, 0, (1920, 0)],
            self.lowerDiagonalPanel2: [3840, -1920, (3840, -1920)],
        }
        self.screen = screen

    def drawSpace(self, dt):
        self.moveBackground(dt)

        for background in self.backgroundPositions:
            self.screen.blit(background, (self.backgroundPositions[background][0], self.backgroundPositions[background][1]))
    
    def moveBackground(self, dt):
        for background in self.backgroundPositions:
            self.backgroundPositions[background][0] -= int(1 * (dt/6))
            self.backgroundPositions[background][1] += int(1 * (dt/6))
            self.checkPanelPosition(background)
    
    def checkPanelPosition(self, panel):
        xPos = self.backgroundPositions[panel][0]
        yPos = self.backgroundPositions[panel][1]
        if panel == self.upperDiagonalPanel or panel == self.upperDiagonalPanel2:
            # check upper positions (-1920, 0) ** hard coded 1920x1920 dimensions
            if xPos <= -1920 and yPos >= 0:
                self.rebufferPanel(panel, 1920, -3840)
        elif panel == self.centerDiagonalPanel or panel == self.centerDiagonalPanel2:
            # check center positions (-1920, 1080)
            if xPos <= -1920 and yPos >= 1920:
                self.rebufferPanel(panel, 1920, -1920)
        elif panel == self.lowerDiagonalPanel or panel == self.lowerDiagonalPanel2:
            # check lower positions (0, 1080)
            if xPos <= 0 and yPos >= 1920:
                self.rebufferPanel(panel, 3840, -1920)

    
    def rebufferPanel(self, panel, newX, newY):
        self.backgroundPositions[panel][0] = newX
        self.backgroundPositions[panel][1] = newY