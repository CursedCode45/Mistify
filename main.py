import pygame as pg
import numpy as np
import random
import math
import time
import sys


WIDTH = 1600
HEIGHT = 900
FPS = 60
TITLE = "Mistify"


class Point:
    def __init__(self, app, dirX, dirY, speed):
        self.app = app
        self.speed = speed
        self.size = 2
        self.color = (255, 255, 255)
        self.position = np.array([random.uniform(1, self.app.width-1), random.uniform(1, self.app.height-1)], dtype="float64")
        self.velocity = np.array([self.speed*dirX, self.speed*dirY], dtype="float64")


    def isOutOfScreen(self):
        if self.position[0] > self.app.width or self.position[0] < 0:
            self.velocity[0] *= (-1)
        if self.position[1] > self.app.height or self.position[1] < 0:
            self.velocity[1] *= (-1)


    def update(self):
        self.isOutOfScreen()
        self.position += self.velocity


    def draw(self):
        pg.draw.circle(app.screen, self.color, (self.position[0], self.position[1]), self.size)



class Line:
    def __init__(self, app, color):
        self.app = app
        self.color = color
        self.p1 = Point(self.app, 1, 1, 3)
        self.p2 = Point(self.app, -1, -1, 5)


    def update(self):
        self.p1.update()
        self.p2.update()


    def drawPoints(self):
        self.p1.draw()
        self.p2.draw()


    def draw(self):
        self.update()
        pg.draw.line(self.app.screen, self.color, (self.p1.position[0], self.p1.position[1]),
                                                  (self.p2.position[0], self.p2.position[1]))


class App:
    def __init__(self, width, height, fps, title):
        pg.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.title)
        self.clock = pg.time.Clock()
        self.line1 = Line(self, (64,224,208))
        self.line2 = Line(self, (250,128,114))
        self.black_rect = pg.Surface((self.width, self.height), pg.SRCALPHA)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            pass
        if keys[pg.K_d]:
            pass
        if keys[pg.K_w]:
            pass
        if keys[pg.K_s]:
            pass


    def update_screen(self):
        pg.display.set_caption(str(self.clock.get_fps()))
        self.black_rect.fill((0, 0, 0, 1))
        self.screen.blit(self.black_rect, (0, 0))
        self.line1.draw()
        self.line2.draw()
        pg.display.update()


    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.check_events()
            self.update_screen()


if __name__ == "__main__":
    app = App(WIDTH, HEIGHT, FPS, TITLE)
    app.run()