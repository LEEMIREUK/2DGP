import gfw
import random
from pico2d import *
from bossbullet import BossBullet

class Boss:
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height()
        self.image = gfw.image.load('res/boss.png')
        self.hit_image = gfw.image.load('res/hit_boss.png')
        self.width = 318
        self.height = 192
        self.half_image_width = self.width // 2
        self.half_image_height = self.height // 2
        self.speed = 50
        self.delta = Boss.init_delta(self)
        self.move = False
        self.hit = False
        self.shoot_time = 0
        self.shooting_interval = 2

        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_UP, BOUNDARY_DOWN
        BOUNDARY_LEFT = 50
        BOUNDARY_RIGHT = get_canvas_width() - 50
        BOUNDARY_UP = get_canvas_height() - 50
        BOUNDARY_DOWN = get_canvas_height() // 2 + 50

    def init_delta(self):
        dx = random.random()
        if dx < 0.5: dx -= 1
        dy = random.random()
        if dy < 0.5: dy -= 1
        return dx, dy

    def draw(self):
        if self.hit:
            self.hit_image.draw(*self.pos, 318, 192)
            self.hit = False
        else:
            self.image.draw(*self.pos, 318, 192)

    def fire(self):
        x, y = self.pos
        self.shoot_time = 0
        boss_bullet = BossBullet((x - 140, y - 60))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x - 140, y - 100))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x - 100, y - 60))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x - 100, y - 100))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

        boss_bullet = BossBullet((x + 140, y - 60))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x + 140, y - 100))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x + 100, y - 60))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        boss_bullet = BossBullet((x + 100, y - 100))
        gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

    def update(self):
        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_UP, BOUNDARY_DOWN
        x, y = self.pos
        dx, dy = self.delta

        if not self.move:
            if y > get_canvas_height() // 2 + 200:
                y -= self.speed * gfw.delta_time
            else:
                self.move = True
        if self.move:
            self.shoot_time += gfw.delta_time
            if self.shoot_time >= self.shooting_interval:
                self.fire()

            # left
            if x < BOUNDARY_LEFT + self.half_image_width:
                dx = random.random()
                if dx < 0.5: dx -= 1  # dx: -1.0 ~ -0.5, +0.5 ~ +1.0
                if dx < 0:
                    dx = -dx
            # right
            if x > BOUNDARY_RIGHT - self.half_image_width:
                dx = random.random()
                if dx < 0.5: dx -= 1  # dx: -1.0 ~ -0.5, +0.5 ~ +1.0
                if dx > 0:
                    dx = -dx
            # up
            if y > BOUNDARY_UP - self.half_image_height:
                dy = random.random()
                if dy < 0.5: dy -= 1  # dy: -1.0 ~ -0.5, +0.5 ~ +1.0
                if dy > 0:
                    dy = -dy
            # down
            if y < BOUNDARY_DOWN + self.half_image_height:
                dy = random.random()
                if dy < 0.5: dy -= 1  # dy: -1.0 ~ -0.5, +0.5 ~ +1.0
                if dy < 0:
                    dy = -dy

            x += dx * self.speed * gfw.delta_time
            y += dy * self.speed * gfw.delta_time

        self.delta = dx, dy
        self.pos = x, y

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)