import gfw
from pico2d import *

class Boss:
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.image = gfw.image.load('res/boss.png')

    def draw(self):
        self.image.draw(*self.pos, 318, 192)

    def update(self):
        pass

    def remove(self):
        pass