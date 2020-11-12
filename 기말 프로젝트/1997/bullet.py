import gfw
from pico2d import *

class Bullet:
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
        x,y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time
        self.pos = x,y

        if y < 0:
            EnemyBullet.remove(self)

    def set_target(self, target):
        x, y = self.pos
        tx, ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)