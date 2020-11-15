import gfw
import random
import stage1
from pico2d import *
from enemybullet import EnemyBullet

class Enemy:
    SIZE = 32
    def __init__(self):
        self.pos = (
            random.randint(-100, get_canvas_width() + 100),
            random.randint(get_canvas_height(), get_canvas_height() + 100)
        )
        self.delta = 0, 0
        self.image = gfw.image.load('res/enemy.png')
        self.fidx = 0
        self.player = gfw.world.object(gfw.layer.player, 0)

        # enemy remove info
        self.die = False
        self.explosion_image = gfw.image.load('res/enemy_explosion.png')
        self.explosion_fidx = 0
        self.explosion_time = 0

        # enemy 총알 발사 info
        self.shoot_time = 0
        self.shooting_interval = 0

        # enemy 난이도 정보
        self.time = stage1.get_playertime()
        if self.time >= 0 and self.time < 20:
            self.speed = random.randint(40, 60)
            self.shooting_interval = 2
        elif self.time >= 20 and self.time < 40:
            self.speed = random.randint(60, 120)
            self.shooting_interval = 1.5
        else:
            self.speed = random.randint(200, 240)
            self.shooting_interval = 1

        Enemy.set_target(self, (self.player.x, self.player.y))

    def explosion(self):
        self.die = True

    def fire(self):
        des = self.player.x, self.player.y
        self.shoot_time = 0
        enemy_bullet = EnemyBullet(self.pos, des)
        gfw.world.add(gfw.layer.enemy_bullet, enemy_bullet)

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
            x, y = self.pos
            dx, dy = self.delta
            x += dx * self.speed * gfw.delta_time
            y += dy * self.speed * gfw.delta_time
            if y < -(Enemy.SIZE // 2):
                Enemy.remove(self)
            self.pos = x, y
        else:
            self.explosion_time += 1
            if self.explosion_time % 5 == 1:
                self.explosion_fidx += 1
                if self.explosion_fidx == 6:
                    Enemy.remove(self)

        # enemy shooting
        self.shoot_time += gfw.delta_time
        if self.shoot_time >= self.shooting_interval:
            self.fire()

    def set_target(self, target):
        x, y = self.pos
        tx, ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0: return

        self.delta = dx / distance, dy / distance

    def get_bb(self):
        x, y = self.pos
        half = Enemy.SIZE // 2
        return x - half, y - half, x + half, y + half

    def remove(self):
        gfw.world.remove(self)