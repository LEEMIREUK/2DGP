import gfw
import stage
import random
from pico2d import *

class BossBullet:
    SIZE = 16
    def __init__(self, boss_pos, des):
        self.pos = (boss_pos[0], boss_pos[1])
        self.size = 16, 16
        self.image = gfw.image.load('res/boss_bullet.png')
        self.speed = 100
        self.delta = 0, 0
        self.des = des
        BossBullet.set_target(self)

    def draw(self):
        self.image.draw(*self.pos, *self.size)

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        if x < 0 or x > get_canvas_width():
            BossBullet.remove(self)
        if y < 0 or y > get_canvas_height():
            BossBullet.remove(self)

        self.pos = x, y

    def set_target(self):
        x, y = self.pos
        tx, ty = self.des
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return
        self.delta = dx / distance, dy / distance

    def get_bb(self):
        x, y = self.pos
        h = BossBullet.SIZE // 2
        return x - h, y - h, x + h, y + h

    def remove(self):
        stage.score += 500
        gfw.world.remove(self)
