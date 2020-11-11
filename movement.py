import pygame
class player(object):
    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, SPRITE_OFFSET):
        self.wh = WINDOW_HEIGHT
        self.ww = WINDOW_WIDTH
        self.offset = SPRITE_OFFSET
        self.playerPos = [int(WINDOW_HEIGHT/2), WINDOW_WIDTH-SPRITE_OFFSET]

# All of our player's movement is handled here.
    def act(self, keys, dt):
        if keys[pygame.K_a]:
            self.playerPos[0] -= 1 * dt
        if keys[pygame.K_d]:
            self.playerPos[0] += 1 * dt
        if keys[pygame.K_w]:
            self.playerPos[1] -= 1 * dt
        if keys[pygame.K_s]:
            self.playerPos[1] += 1 * dt

    def gravity(self, dt):
        if self.playerPos[1] < self.ww-self.offset:
            self.playerPos[1] += 1 * dt

    def retrievePosition(self):
        return self.playerPos