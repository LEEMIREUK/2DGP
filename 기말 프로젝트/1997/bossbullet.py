import gfw
import stage
from pico2d import *

class BossBullet:
    SIZE = 16
    def __init__(self):
        self.pos = get_canvas_width() // 2, 50
        self.size = 16, 16
        self.image = gfw.image.load('res/boss_bullet.png')

        # self.time = stage.get_playertime()

    def draw(self):
        self.image.draw(*self.pos, *self.size)

    def update(self):
        pass

    def get_bb(self):
        x, y = self.pos
        h = BossBullet.SIZE // 2
        return x - h, y - h, x + h, y + h

    def remove(self):
        pass