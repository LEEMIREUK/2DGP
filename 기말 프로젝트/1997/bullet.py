import gfw
import gobj
from pico2d import *

class Bullet:
    bullets = []
    SIZE = 50
    def __init__(self, x, y, speed, upgrade):
        self.x, self.y = x, y
        self.dy = speed
        self.bullet_level = upgrade
        self.image = gfw.image.load('res/player1_bullet1.png')
        self.damage =10

    def draw(self):
        width, height = 15, 34
        sx = (self.bullet_level - 1) * width
        if self.bullet_level == 1:
            self.image.clip_draw(sx, 0, width, height, self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time
        if self.y > get_canvas_height() - 100:
            self.remove()

    def remove(self):
        gfw.world.remove(self)