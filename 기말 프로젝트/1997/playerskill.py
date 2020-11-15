import gfw
from pico2d import *

class PlayerSkill:
    skills = []
    def __init__(self, x, y):
        self.x, self.y = x, y + get_canvas_height() // 2 + 50
        self.image = gfw.image.load('res/razer_skill.png')
        self.damage = 100
        self.fidx = 0
        self.time = 0
        self.width = 33
        self.height = 869

    def draw(self):
        sx = self.fidx * self.width
        self.image.clip_draw(sx, 0, self.width, self.height, self.x, self.y)

    def update(self):
        self.time += 1
        if self.time % 5 == 1:
            self.fidx += 1
            if self.fidx == 16:
                PlayerSkill.remove(self)

    def get_bb(self):
        hw = self.width // 2
        hh = self.height // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

    def remove(self):
        gfw.world.remove(self)