import gfw
import random
from pico2d import *
from bossbullet import BossBullet

class Boss:
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() + 150
        self.image = gfw.image.load('res/boss.png')
        self.hit_image = gfw.image.load('res/hit_boss.png')
        self.explosion_image = gfw.image.load('res/boss_explosion.png')
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
        self.shoot_mode = 0
        self.time = 0
        self.hp = 1000


        self.die = False
        self.explosion_time = 0
        self.explosion_frame = 0

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
        if self.die:
            self.explosion_image.clip_draw(self.explosion_frame * 32, 0, 32, 32, *self.pos, 192, 192)
            return

        if self.hit:
            self.hit_image.draw(*self.pos, 318, 192)
            self.hit = False
        else:
            self.image.draw(*self.pos, 318, 192)

    def fire(self, mode):
        x, y = self.pos
        self.shoot_time = 0
        if mode == 0:
            des1 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x - 140, y - 60), des1)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des2 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x - 140, y - 100), des2)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des3 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x - 100, y - 60), des3)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des4 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x - 100, y - 100), des4)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des5 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x + 140, y - 60), des5)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des6 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x + 140, y - 100), des6)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des7 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x + 100, y - 60), des7)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            des8 = (random.randint(0, get_canvas_width()), 0)
            boss_bullet = BossBullet((x + 100, y - 100), des8)
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
        elif mode == 1:
            des = (0, 0)
            boss_bullet = BossBullet((x - 140, y - 60), (des))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x - 140, y - 100), (des[0] + 85, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x - 100, y - 60), (des[0] + 170, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x - 100, y - 100), (des[0] + 255, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

            boss_bullet = BossBullet((x + 140, y - 60), (des[0] + 340, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x + 140, y - 100), (des[0] + 425, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x + 100, y - 60), (des[0] + 510, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)
            boss_bullet = BossBullet((x + 100, y - 100), (des[0] + 600, des[1]))
            gfw.world.add(gfw.layer.boss_bullet, boss_bullet)

    def update(self):
        if self.die:
            self.explosion_time += 1
            if self.explosion_time % 10:
                self.explosion_frame += 1
                if self.explosion_time == 12:
                    Boss.remove(self)
            return

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
            self.time += 1
            if self.time % 500 == 1:
                self.shoot_mode = random.randint(0, 1)

            if self.shoot_mode == 0:
                if self.shoot_time >= self.shooting_interval:
                    self.fire(0)
            if self.shoot_mode == 1:
                if self.shoot_time >= self.shooting_interval - 1:
                    self.fire(1)

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

    def explosion(self):
        self.die = True

    def get_bb(self):
        x, y = self.pos
        hw = self.width // 2
        hh = self.height // 2
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)
        print("승리")