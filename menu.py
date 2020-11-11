import pygame

class menu:
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH):
        font = pygame.font.SysFont('couriernew', 56)
        self.text = font.render("Press 'r' to resume game", True, (0, 128, 0))
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH = WINDOW_WIDTH
    
    def drawMenu(self, screen):
        xPos = int(self.WINDOW_HEIGHT/3)
        yPos = int(self.WINDOW_WIDTH/2)
        screen.blit(self.text, (xPos, yPos))