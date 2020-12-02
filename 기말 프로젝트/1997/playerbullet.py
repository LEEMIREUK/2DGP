import gfw
from pico2d import *

class PlayerBullet:
    def __init__(self, x, y, speed, upgrade):
        self.x, self.y = x, y
        self.dy = speed
        self.bullet_level = upgrade
        self.image = gfw.image.load('res/player1_bullet1.png')
        self.upgrade_image = gfw.image.load('res/player1_bullet2.png')
        if upgrade == 1:
            self.damage = 5
        elif upgrade == 2:
            self.damage = 5
        elif upgrade == 3:
            self.damage = 15
        elif upgrade == 4:
            self.damage = 30

        self. width, self.height = 15, 34
        self.upgrade_width, self.upgrade_height = 50, 60

    def draw(self):
        width = self.width * self.bullet_level
        if self.bullet_level < 4:
            self.image.clip_draw(0, 0, width, self.height, self.x, self.y)
        else:
            self.upgrade_image.clip_draw(0, 0, self.upgrade_width, self.upgrade_height, self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time
        if self.y > get_canvas_height():
            self.remove()

    def get_bb(self):
        if self.bullet_level < 4:
            hw = self.width // 2 * self.bullet_level
            hh = self.height // 2
        else:
            hw = self.upgrade_width // 2
            hh = self.upgrade_height // 2

        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

    def remove(self):
        gfw.world.remove(self)