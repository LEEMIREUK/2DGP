from pico2d import *
from gobj import *

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.type) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

open_canvas()

grass = Grass()
team = [ Boy() for i in range(11) ] 

running = True

while running:
    clear_canvas()
    grass.draw()
    for b in team: b.draw()
    update_canvas()

    handle_events()
    
    for b in team: b.update()

    delay(0.01)

close_canvas()
    

    
