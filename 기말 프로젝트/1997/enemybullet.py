import gfw
from pico2d import *

class EnemyBullet:
    def __init__(self, departure, destination):
        self.pos = departure
        self.des = destination
        self.speed = 100
        self.delta = 0, 0
        self.width = 10
        self.height = 10
        self.image = gfw.image.load('res/enemy_bullet.png')
        EnemyBullet.set_target(self, self.des)

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        if x < 0 or x > get_canvas_width():
            EnemyBullet.remove(self)
        if y < 0 or y > get_canvas_height():
            EnemyBullet.remove(self)
        self.pos = x, y

    def set_target(self, target):
        x, y = self.pos
        tx, ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return

        self.delta = dx / distance, dy / distance

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)