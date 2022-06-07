import sys
import pygame
from settings import settings
from object import Block


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.get_res())
        pygame.display.set_caption('exp')
        self.clock = pygame.time.Clock()

        self.floor_h = 400
        self.num_of_col = 0
        self.block1 = Block(300, self.floor_h, 20, 20, m=1, v=0)
        self.block2 = Block(500, self.floor_h, 30, 30, m=10000, v=-1)
        self.wall = Block(100, 540, 10, 200, 0, 0)

    def draw(self):
        self.screen.blit(self.block1.surf, dest=(self.block1.x, self.block1.y))
        self.screen.blit(self.block2.surf, dest=(self.block2.x, self.block2.y))
        self.screen.blit(self.wall.surf, dest=(self.wall.x, self.wall.y))

    def collide(self):
        if self.block1.x + self.block1.w >= self.block2.x:
            self.num_of_col += 1
            print(self.num_of_col)
            return True

    def collide_wall(self):
        if self.block1.x <= self.wall.x + self.wall.w:
            self.block1.v *= -1
            self.num_of_col += 1
            print(self.num_of_col)

    def bounce(self):
        mmod1 = (self.block1.m - self.block2.m) / (self.block1.m + self.block2.m)
        mmod2 = (self.block2.m - self.block1.m) / (self.block1.m + self.block2.m)
        v1 = self.block1.v
        v2 = self.block2.v
        sum_m = self.block1.m + self.block2.m

        self.block1.v = mmod1 * v1 + (2 * self.block2.m / sum_m * v2)
        self.block2.v = (2 * self.block1.m / sum_m * v1) + mmod2 * v2

    def update(self):
        self.collide_wall()
        if self.collide():
            self.bounce()

        self.block1.x += self.block1.v
        self.block2.x += self.block2.v

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('gray')

            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(settings.get_fps())


if __name__ == '__main__':
    game = Game()
    game.run()
