import gfw
from pico2d import *

class PlayerBullet:
    def __init__(self, x, y, speed, upgrade):
        self.x, self.y = x, y
        self.dy = speed
        self.bullet_level = upgrade
        self.image = gfw.image.load('res/player1_bullet1.png')
        self.damage = 10
        self. width, self.height = 15, 34

    def draw(self):
        sx = (self.bullet_level - 1) * self.width
        if self.bullet_level == 1:
            self.image.clip_draw(sx, 0, self.width, self.height, self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time
        if self.y > get_canvas_height():
            self.remove()

    def get_bb(self):
        hw = self.width // 2
        hh = self.height // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

    def remove(self):
        gfw.world.remove(self)