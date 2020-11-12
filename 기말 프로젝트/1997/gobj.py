from pico2d import *
import gfw
import stage1

effect1_on = False
effect2_on = False

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def collides_box(a, b):
    (la, ba, ra, ta) = a.get_bb()
    (lb, bb, rb, tb) = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ba > tb: return False
    if ta < bb: return False

    return True

def draw_collision_box():
    for obj in gfw.world.all_objects():
        if hasattr(obj, 'get_bb'):
            draw_rectangle(*obj.get_bb())

class MainImage:
    def __init__(self):
        self.image = gfw.image.load('res/main_image.png')
        self.pos = (get_canvas_width() // 2, get_canvas_height() // 2)
        self.fidx = 0

    def draw(self):
        width, height = 224, 320
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, *self.pos, 600, 900)

    def update(self):
        self.fidx = (self.fidx + 1) % 20

class StartImage:
    def __init__(self):
        self.image = gfw.image.load('res/start_image.png')
        self.pos = (get_canvas_width() // 2, 300)
        self.fidx = 0
        self.time =0

    def draw(self):
        width, height = 346, 142
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, *self.pos, 150, 75)

    def update(self):
        if effect1_on:
            if self.fidx < 4:
                self.fidx += 1
            elif self.fidx == 4:
                gfw.change(stage1)

class ExitImage:
    def __init__(self):
        self.image = gfw.image.load('res/exit_image.png')
        self.pos = (get_canvas_width() // 2, 200)
        self.fidx = 0
        self.time = 0

    def draw(self):
        width, height = 253, 142
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, *self.pos, 130, 75)

    def update(self):
        if effect2_on:
            if self.fidx < 4:
                self.fidx += 1

class ButtonImage:
    def __init__(self):
        self.image = gfw.image.load('res/button_image.png')
        self.x, self.y = 175, 300
        self.fidx = 0
        self.time = 0

    def draw(self):
        width, height = 15, 15
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, self.x, self.y, 50, 50)

    def update(self):
        self.time += 1
        if self.time % 30 == 1:
            self.fidx = (self.fidx + 1) % 2

    def handle_event(self, e):
        global effect1_on, effect2_on
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.y == 300:
                self.y = 200
            elif self.y == 200:
                self.y = 300
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.y == 200:
                self.y = 300
            elif self.y == 300:
                self.y = 200
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.y == 300:
                effect1_on = True
            elif self.y == 200:
                effect2_on = True
                gfw.quit()

class Stage1Map:
    def __init__(self):
        self.image = gfw.image.load('res/stage1_map.png')
        self.x, self.y = get_canvas_width() // 2, 3500
        self.speed = 30 * gfw.delta_time

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > -2700:
            self.y -= self.speed