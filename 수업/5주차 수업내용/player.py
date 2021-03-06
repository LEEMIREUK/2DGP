import random
from pico2d import *
import gfw
import gfw_image
from gobj import *
from bullet import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1,
        (SDL_KEYDOWN, SDLK_RIGHT):  1,
        (SDL_KEYUP, SDLK_LEFT):     1,
        (SDL_KEYUP, SDLK_RIGHT):   -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    LASER_INTERVAL = 0.25
    SPARK_INTERVAL = 0.05
    IMAGE_RECTS = [
        (  7, 0, 42, 80),
        ( 77, 0, 42, 80),
        (143, 0, 50, 80),
        (207, 0, 56, 80),
        (271, 0, 62, 80),
        (335, 0, 70, 80),
        (407, 0, 62, 80),
        (477, 0, 56, 80),
        (549, 0, 48, 80),
        (621, 0, 42, 80),
        (689, 0, 42, 80),
    ]
    MAX_ROLL = 2.0


    def __init__(self):
        self.x, self.y = 250, 80
        self.dx = 0
        self.speed = 3
        self.image = gfw_image.load(RES_DIR + '/fighters.png')
        self.spark = gfw_image.load(RES_DIR + '/laser_0.png')
        self.src_rect = Player.IMAGE_RECTS[5]
        half = self.src_rect[2] // 2
        self.minx = half
        self.maxx = get_canvas_width() - half
        self.laser_time = 0
        self.roll_time = 0

    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y, 5)
        LaserBullet.bullets.append(bullet)

    def draw(self):
        self.image.clip_draw(*self.src_rect, self.x, self.y)
        if self.laser_time < Player.SPARK_INTERVAL:
            self.spark.draw(self.x, self.y + 28)

    def update(self):
        self.x += self.dx * self.speed
        self.laser_time += gfw.delta_time
        if self.x < self.minx:
            self.x = self.minx
        elif self.x > self.maxx:
            self.x = self.maxx

        dx = self.dx
        if dx == 0:
            if self.roll_time > 0:
                dx = -1
            elif self.roll_time < 0:
                dx = 1
        self.roll_time += dx * gfw.delta_time
        if self.roll_time < -Player.MAX_ROLL:
            self.roll_time = -Player.MAX_ROLL
        elif self.roll_time > Player.MAX_ROLL:
            self.roll_time = Player.MAX_ROLL

        roll = int(self.roll_time * 5 / Player.MAX_ROLL)
        self.src_rect = Player.IMAGE_RECTS[roll + 5]
        
        if self.laser_time >= Player.LASER_INTERVAL:
            self.fire()

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.dx += Player.KEY_MAP[pair]

if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RECTS:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2