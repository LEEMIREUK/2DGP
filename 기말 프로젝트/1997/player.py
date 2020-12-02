import gfw
import collision
from pico2d import *
from playerbullet import PlayerBullet
from playerskill import PlayerSkill

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
    KEYDOWN_LCTRL = (SDL_KEYDOWN, SDLK_LCTRL)
    KEYDOWN_LSHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    SHOOT_INTERVAL = 0.5
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
    LIFE = 4

    def __init__(self):
        self.start_image = gfw.image.load('res/player1_start_animation.png')
        self.image = gfw.image.load('res/player1_animation.png')
        self.speed = 200
        self.end = False

        #image size info
        self.image_size_width = 23
        self.image_size_height = 31
        self.image_rect = Player.IMAGE_RECTS[3]
        self.left_over = self.image_size_width // 2
        self.right_over = get_canvas_width() - (self.image_size_width // 2)
        self.down_over = self.image_size_height // 2
        self.up_over = get_canvas_height() - (self.image_size_height // 2)

        self.explosion_image = gfw.image.load('res/player1_explosion.png')

        Player.resetinfo(self)

    def resetinfo(self):
        self.x, self.y = get_canvas_width() // 2, -60
        self.delta = 0, 0
        self.frame = 0
        self.time = 0
        self.roll_time = 0
        self.invic_frame = 0
        self.invic_time = 0

        # player explosion info
        self.die = False
        self.explosion_frame = 0
        self.explosion_time = 0

        # player bullet info
        self.shoot_speed = 200
        self.upgrade = 1

        global invincibility
        invincibility = True

        global moving
        moving = False

        if Player.LIFE == 4:
            Player.LIFE = 3
        elif Player.LIFE == 3:
            Player.LIFE = 2
        elif Player.LIFE == 2:
            Player.LIFE = 1
        elif Player.LIFE == 1:
            self.end = True

    def fire(self):
        bullet = PlayerBullet(self.x, self.y + self.image_size_height // 2,
                              self.shoot_speed, self.upgrade)
        gfw.world.add(gfw.layer.bullet, bullet)

    def skill(self):
        skill = PlayerSkill(self.x, self.y)
        gfw.world.add(gfw.layer.skill, skill)

    def explosion(self):
        self.die = True


    def draw(self):
        width, height = 23, 31
        exp_width, exp_height = 32, 32
        ex = self.explosion_frame * exp_width
        sx = self.frame * width
        if not self.die:
            #처음 부분 = 무적 + 움직x
            if invincibility and not moving:
                if (self.invic_frame % 2) == 1:
                    self.start_image.clip_draw(sx, 0, width, 117, self.x, self.y)
            # 무적 + 움직 o
            if invincibility and moving:
                if (self.invic_frame % 2) == 1:
                    self.image.clip_draw(*self.image_rect, self.x, self.y)
            # 무적 X + 움직
            if not invincibility and moving:
                self.image.clip_draw(*self.image_rect, self.x, self.y)

        else:
            self.explosion_image.clip_draw(ex, 0, exp_width, exp_height, self.x, self.y)

    def update(self):
        global invincibility
        if invincibility:
            self.invic_frame += 0.5

        if not self.die:
            if not moving:
                Player.start_motion(self)
            else:
                dx, dy = self.delta
                self.x += dx * self.speed * gfw.delta_time
                self.y += dy * self.speed * gfw.delta_time
                self.x = clamp(self.left_over, self.x, self.right_over)
                self.y = clamp(self.down_over, self.y, self.up_over)
                self.update_roll()
                self.invic_time += gfw.delta_time
                if self.invic_time >= 1:
                    invincibility = False
        else:
            self.explosion_time += 1
            if self.explosion_time % 5:
                self.explosion_frame += 1
                if self.explosion_time == 14:
                    Player.dead(self)

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
        if moving:
            pair = (e.type, e.key)
            if pair in Player.KEY_MAP:
                self.delta = collision.point_add(self.delta, Player.KEY_MAP[pair])
        else:
            return
        if not invincibility:
            pair = (e.type, e.key)
            if pair== Player.KEYDOWN_LCTRL:
                Player.fire(self)
            if pair == Player.KEYDOWN_LSHIFT:
                Player.skill(self)
        else:
            return

    def start_motion(self):
        global moving
        self.y += 1
        self.time += 1
        if self.time % 15 == 1:
            self.frame += 1

        if self.frame == 9:
            self.frame = 3
            self.y += 43
            moving = True

    def get_bb(self):
        hw = self.image_rect[2] / 2
        hh = self.image_rect[3] / 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

    def dead(self):
        Player.__init__(self)

    def returninfo(self):
        global invincibility
        return invincibility

    def remove(self):
        gfw.world.remove(self)
        # 게임 오버