import gfw
import random
from pico2d import *

class Enemy:
    SIZE = 32
    def __init__(self):
        self.pos = (
            random.randint(-100, get_canvas_width() + 100),
            random.randint(get_canvas_height(), get_canvas_height() + 100)
        )
        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
        self.delta = 0, 0
        self.image = gfw.image.load('res/enemy.png')
        self.explosion_image = gfw.image.load('res/enemy_explosion.png')
        self.explosion_fidx = 0
        self.explosion_time = 0
        self.fidx = 0
        self.player = gfw.world.object(gfw.layer.player, 0)
        self.destination = 0, 0
        self.die = False
        self.time = self.player.play_time
        if self.time >= 0 and  self.time < 20:
            self.speed = random.randint(40, 60)
        elif self.time >= 20 and self.time < 40:
            self.speed = random.randint(60, 140)
        elif self.time >= 40:
            self.speed = random.randint(140, 200)

    def explosion(self):
        self.die = True

    def draw(self):
        width, height = 32, 32
        exp_width, exp_height = 32, 32
        ex = self.explosion_fidx * exp_width
        sx = self.fidx * width
        if not self.die:
            self.image.clip_draw(sx, 0, width, height, *self.pos)
        else:
            self.explosion_image.clip_draw(ex, 0, exp_width, exp_height, *self.pos)

    def update(self):
        if not self.die:
            self.fidx = (self.fidx + 1) % 3
            Enemy.set_target(self, (self.player.x, self.player.y))
            x,y = self.pos
            dx,dy = self.delta
            x += dx * self.speed * gfw.delta_time
            y += dy * self.speed * gfw.delta_time
            tx,ty = self.target
            if dx > 0 and x >= tx or dx < 0 and x <= tx:
                x = tx
            if dy > 0 and y >= ty or y < 0 and y <= ty:
                y = ty
            self.pos = x,y
        else:
            self.explosion_time += 1
            if self.explosion_time % 5 == 1:
                self.explosion_fidx += 1
                if self.explosion_fidx == 6:
                    Enemy.remove(self)

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
        half = Enemy.SIZE // 2
        return x - half, y - half, x + half, y + half

    def remove(self):
        gfw.world.remove(self)