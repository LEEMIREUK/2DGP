from pico2d import *
import gfw
import main_state

canvas_width = 600
canvas_height = 800

def enter():
    global logo, elapsed
    logo = gfw.image.load('res/title.png')
    elapsed = 0

    global music_logo
    music_logo = load_wav('sound/logo.wav')
    music_logo.set_volume(30)
    music_logo.play(1)

def update():
    global elapsed
    elapsed += gfw.delta_time
    if elapsed > 1.0:
        gfw.change(main_state)

def draw():
    logo.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

def exit():
    global logo, music_logo
    gfw.image.unload('res/title.png')
    del logo
    del music_logo

if __name__ == '__main__':
    gfw.run_main()