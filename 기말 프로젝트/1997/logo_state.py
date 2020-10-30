from pico2d import *
import gfw
import main_state

canvas_width = 600
canvas_height = 600

def enter():
    global image, elapsed
    image = load_image('res/title.png')
    elapsed = 0

def update():
    global elapsed
    elapsed += gfw.delta_time
    if elapsed > 1.0:
        close_canvas()
        gfw.change(main_state)

def draw():
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 600)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

def exit():
    global image
    del image

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()