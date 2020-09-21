from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')
    def draw(self):
        self.image.draw(400, 30)
        
class Boy:
    def __init__(self, x=0, y=85, dx=2):
        self.image = load_image('../res/animation_sheet.png')
        self.x, self.y = x, y
        self.frame_index = 0
        self.action = 0
        self.dx = dx

    def draw(self):
        self.image.clip_draw(100 * self.frame_index, 100 * self.action, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.dx
        self.frame_index = (self.frame_index + 1) % 8
        if self.x % 100 == 0:
            self.action = (self.action + 1) % 4
        
open_canvas()

# type name = UpperCamelCase
# method name = lowerCamelCase
grass = Grass()
boy = Boy()
b2 = Boy(get_canvas_width(), 200, -2)

#objects = [ grass, boy, b2 ]

running = True

while running:
    clear_canvas()
    #for o in objects:
    #    o.draw()

        #if o is Grass:
        #    o.image.draw(400, 300)
        #else:
        #    o.image.clip_draw(100 * o.frame_index, 100 * o.action, 100, 100, o.x, 85)

    grass.draw()
    boy.draw()
    b2.draw()
    update_canvas()

    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.type) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

    boy.update()
    b2.update()
        
    if boy.x > get_canvas_width():
        running = False

    delay(0.02)

close_canvas()
    

    
