import gfw
import stage
import random
from pico2d import *

class EnemyBullet:
    SIZE = 10
    def __init__(self, departure, destination):
        self.pos = departure
        self.des = destination
        self.delta = 0, 0
        self.width = 10
        self.height = 10
        self.image = gfw.image.load('res/enemy_bullet.png')

        self.time = stage.get_playertime()
        if self.time >= 0 and self.time < 20:
            self.speed = random.randint(150, 200)
        elif self.time >= 20 and self.time < 40:
            self.speed = random.randint(200, 250)
        else:
            self.speed = random.randint(250, 300)

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
        h = EnemyBullet.SIZE // 2
        return x - h, y - h, x + h, y + h

    def remove(self):
        gfw.world.remove(self)