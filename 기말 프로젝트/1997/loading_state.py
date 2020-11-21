import gobj
import gfw
import stage
from pico2d import *

# canvas_width = 600
# canvas_height = 800

def enter():
    global loading
    loading = gfw.image.load('res/player1_loading.png')

    global loading_time
    loading_time = 1

def update():
    global loading_time
    loading_time -= gfw.delta_time
    if loading_time <= 0:
        gfw.change(stage)

def draw():
    loading.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            pass

def exit():
    global loading
    gfw.image.unload('res/player1_loading.png')
    del loading

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()