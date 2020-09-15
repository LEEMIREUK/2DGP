from pico2d import *

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False

open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')


running = True
x= 0
fidx = 0
while running and x < 800:
    clear_canvas()
    gra.draw(400, 30)
    ch.clip_draw(fidx*100, 0, 100, 100, x, 85)
    update_canvas()


    handle_events()

    fidx = (fidx + 1) % 8
    x += 3
    delay(0.01)

close_canvas()
    

    
