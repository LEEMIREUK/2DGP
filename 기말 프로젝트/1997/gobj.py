from pico2d import *
import gfw
import main_state

effect1_on = False
effect2_on = False

class MainImage:
    def __init__(self, image):
        self.image = gfw.image.load('res/' + image)
        self.pos = (get_canvas_width() // 2, get_canvas_height() // 2)
        self.fidx = 0

    def draw(self):
        width, height = 224, 320
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, *self.pos, 600, 900)

    def update(self):
        self.fidx = (self.fidx + 1) % 20

class StartImage:
    def __init__(self, image):
        self.image = gfw.image.load('res/' + image)
        self.pos = (get_canvas_width() // 2, 300)
        self.fidx = 0
        self.time =0

    def draw(self):
        width, height = 346, 142
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, height, *self.pos, 150, 75)

    def update(self):
        global loading_on
        if effect1_on:
            if self.fidx < 4:
                self.fidx += 1
            elif self.fidx == 4:
                main_state.loading_on = True

class ExitImage:
    def __init__(self, image):
        self.image = gfw.image.load('res/' + image)
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
    def __init__(self, image):
        self.image = gfw.image.load('res/' + image)
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

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

class StageMap:
    def __init__(self, image):
        self.image = gfw.image.load('res/' + image)
        self.x, self.y = get_canvas_width() // 2, 3500
        self.speed = 30 * gfw.delta_time

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.y > -2700:
            self.y -= self.speed