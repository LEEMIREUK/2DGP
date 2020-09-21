import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(400, 30)
        
class Boy:
    def __init__(self):
        self.image = load_image('../res/animation_sheet.png')
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 100) + 85
        self.dx = random.random() # 0.0 ~ 1.0
        self.dy = random.random()
        self.frame_index = random.randint(0, 7)
        self.action = random.randint(0, 3)
        

    def draw(self):
        self.image.clip_draw(100 * self.frame_index, 100 * self.action, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.frame_index = (self.frame_index + 1) % 8
        
        if self.x % 100 == 0:
            self.action = (self.action + 1) % 4
        
open_canvas()

grass = Grass()
team = [ Boy() for i in range(11) ] 

#for i in range(11):
#    team.append(Boy())


running = True

while running:
    clear_canvas()
    grass.draw()
    for b in team: b.draw()
    update_canvas()

    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.type) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

    for b in team: b.update()
        
    #if boy.x > get_canvas_width():
    #    running = False

    delay(0.01)

close_canvas()
    

    
