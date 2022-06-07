import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x, floor_h, w, h, m, v):
        super().__init__()
        self.x = x
        self.y = floor_h - h
        self.h = h
        self.w = w
        self.m = m
        self.v = v

        self.surf = pygame.surface.Surface((self.w, self.h))
        self.surf.fill('red')
