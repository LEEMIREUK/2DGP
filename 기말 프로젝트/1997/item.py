import gfw
import random
from pico2d import *

class Item:
    def __init__(self):
        self.image = gfw.image.load('res/item_image.png')
        self.dir = random.randint(1, 3)
        self.speed = 50

        self.time = 0
        self.frame = 0
        self.width = 20
        self.height = 13

        global SIDE_LEFT, SIDE_RIGHT, SIDE_UP, SIDE_DOWN
        SIDE_LEFT =  -self.width // 2
        SIDE_RIGHT = get_canvas_width() + SIDE_LEFT
        SIDE_DOWN = self.height // 2
        SIDE_UP = get_canvas_height() + SIDE_DOWN

        cw, ch = get_canvas_width(), get_canvas_height()
        dx = random.random()
        if dx < 0.5: dx -= 1
        dy = random.random()
        if dy < 0.5: dy -= 1

        side = random.randint(1, 3)
        if side == 1: # left
            x = -self.width // 2
            y = random.random() * ch
            if dx < 0:
                dx = -dx
        elif side == 2: # top
            x = random.random() * cw
            y = ch + self.height // 2
            if dy > 0:
                dy = -dy
        else: # right
            x = get_canvas_width() + self.width // 2
            y = random.random() * ch
            if dx > 0:
                dx = -dx

        self.pos = x, y
        self.delta = dx, dy

    def draw(self):
        self.image.clip_draw(self.frame * self.width, 0, self.width, self.height, *self.pos)

    def update(self):
        self.time += 1
        if self.time % 20 == 1:
            self.frame = (self.frame + 1) % 6

        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        self.pos = x, y

        global SIDE_LEFT, SIDE_RIGHT, SIDE_UP, SIDE_DOWN
        if x < SIDE_LEFT or x > SIDE_RIGHT or y < SIDE_DOWN or y > SIDE_UP:
            Item.remove(self)

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)