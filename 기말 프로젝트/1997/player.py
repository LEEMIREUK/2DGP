import gfw
import gobj
from pico2d import *
from bullet import *

effect = False

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    SHOOT_INTERVAL = 0.25
    IMAGE_RECTS = [
        (1, 0, 21, 31),
        (24, 0, 23, 31),
        (46, 0, 23, 31),
        (69, 0, 23, 31),
        (92, 0, 23, 31),
        (115, 0, 21, 31),
        (138, 0, 21, 31),
    ]
    MAX_ROLL = 0.4

    def __init__(self):
        self.x, self.y = get_canvas_width() // 2, -60
        self.delta = 0, 0
        self.speed = 200
        self.start_image = gfw.image.load('res/player1_start_animation.png')
        self.image = gfw.image.load('res/player1_animation.png')
        self.image_size_width = 23
        self.image_size_height = 31
        self.image_rect = Player.IMAGE_RECTS[3]
        self.left_over = self.image_size_width // 2
        self.right_over = get_canvas_width() - (self.image_size_width // 2)
        self.down_over = self.image_size_height // 2
        self.up_over = get_canvas_height() - (self.image_size_height // 2)

        #animation fidx: 0 ~ 6
        self.fidx = 0
        self.time = 0
        self.roll_time = 0

    def fire(self):
        bullet = Bullet(self.x, self.y + self.image_size_height // 2, 200, 1)
        Bullet.bullets.append(bullet)

    def draw(self):
        width, height = 23, 31
        index = self.fidx * width
        sx = self.fidx * width
        if not effect:
            self.start_image.clip_draw(index, 0, width, 117, self.x, self.y)
        else:
            self.image.clip_draw(*self.image_rect, self.x, self.y)

    def update(self):
        if not effect:
            Player.start_motion(self)
        else:
            dx, dy = self.delta
            self.x += dx * self.speed * gfw.delta_time
            self.y += dy * self.speed * gfw.delta_time
            self.x = clamp(self.left_over, self.x, self.right_over)
            self.y = clamp(self.down_over, self.y, self.up_over)
            self.update_roll()

    def update_roll(self):
        dx = self.delta[0]
        if dx == 0:
            if self.roll_time > 0:
                dx = -1
            elif self.roll_time < 0:
                dx = 1
        self.roll_time += dx * gfw.delta_time
        if self.delta[0] == 0:
            if dx < 0 and self.roll_time < 0:
                self.roll_time = 0
            if dx > 0 and self.roll_time > 0:
                self.roll_time = 0

        self.roll_time = clamp(-Player.MAX_ROLL, self.roll_time, Player.MAX_ROLL)

        roll = int(self.roll_time * 3 / Player.MAX_ROLL)
        self.image_rect = Player.IMAGE_RECTS[roll + 3]

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = gobj.point_add(self.delta, Player.KEY_MAP[pair])
        if pair == Player.KEYDOWN_SPACE:
            if effect:
                Player.fire(self)

    def start_motion(self):
        global effect
        self.y += 1
        self.time += 1
        if self.time % 15 == 1:
            self.fidx += 1

        if self.fidx == 9:
            self.fidx = 3
            self.y += 43
            effect = True