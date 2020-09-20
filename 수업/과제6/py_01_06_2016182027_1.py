from pico2d import *
import helper as h


def handle_events():
    global running, moving
    global dx, dy, tx, ty, x, y ,pos,target,delta
    global speed
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if e.button == SDL_BUTTON_LEFT:
                target = e.x,get_canvas_height() - e.y - 1
                destination.append(target)
                speed += 3
                if not moving:
                    moving = True
                

open_canvas()

gra = load_image('../res/grass.png')
ch = load_image('../res/run_animation.png')

running = True
arrive = False
moving = False

pos = 400, 85
target = 0,0
delta = 0,0
fidx = 0
speed = 1
destination = []

while running:
    clear_canvas()
    gra.draw(400, 30)
    
    ch.clip_draw(fidx * 100, 0, 100, 100, pos[0], pos[1])
    update_canvas()

    handle_events()

    if moving:
        fidx = (fidx + 1) % 8

    if not len(destination) == 0:
        delta = h.delta(pos,destination[0],speed)
        pos,arrive = h.move_toward(pos,delta,destination[0])

    if arrive:  
        speed = 1
        if not len(destination) == 0:
            destination.pop(0)
        else:
            moving = True
            fidx = 0
            
    delay(0.02)

close_canvas()
