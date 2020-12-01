import gfw
import random
from pico2d import *

class Boss:
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height()
        self.image = gfw.image.load('res/boss.png')
        self.width = 318
        self.height = 192
        self.half_image_width = self.width // 2
        self.half_image_height = self.height // 2
        self.speed = 100
        self.delta = Boss.init_delta(self)
        self.move = False

        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_UP, BOUNDARY_DOWN
        BOUNDARY_LEFT = 50
        BOUNDARY_RIGHT = get_canvas_width() - 50
        BOUNDARY_UP = get_canvas_height() - 50
        BOUNDARY_DOWN = get_canvas_height() // 2 + 50

    def init_delta(self):
        dx = random.random()
        if dx < 0.5: dx -= 1
        dy = random.random()
        if dy < 0.5: dy -= 1

        return dx, dy

    def draw(self):
        self.image.draw(*self.pos, 318, 192)

    def update(self):
        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_UP, BOUNDARY_DOWN
        x, y = self.pos
        dx, dy = self.delta
        if y > get_canvas_height() // 2 + 200:
            y -= self.speed * gfw.delta_time
        else:
            if x < BOUNDARY_LEFT + self.half_image_width:
                dx *= -1
                dy *= -1
            if x > BOUNDARY_RIGHT - self.half_image_width:
                dx *= -1
                dy *= -1
            if y < BOUNDARY_DOWN + self.half_image_height:
                dx *= -1
                dy *= -1
            if y > BOUNDARY_UP - self.half_image_height:
                dx *= -1
                dy *= -1

            x += dx * self.speed * gfw.delta_time
            y += dy * self.speed * gfw.delta_time

        self.pos = x, y

    # def random_move(self):
        # global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_UP, BOUNDARY_DOWN
        # x, y = self.pos
        # dx, dy = self.delta
        #
        # if x < BOUNDARY_LEFT + self.half_image_width:
        #     dx = random.random()
        # if x < BOUNDARY_RIGHT - self.half_image_width:
        #     dx = -random.random()
        # if y < BOUNDARY_UP - self.half_image_height:
        #     dy = random.random()
        # if y < BOUNDARY_DOWN + self.half_image_height:
        #     dy = -random.random()
        #
        # x += dx * self.speed * gfw.delta_time
        # y += dy * self.speed * gfw.delta_time

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        pass