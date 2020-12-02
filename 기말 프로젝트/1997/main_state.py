import gfw
import gobj
import loading_state
from pico2d import *

loading_on = False

def enter():
    global main_image, start_image, exit_image, button_image
    gfw.world.init(['main_image', 'start_image', 'exit_image', 'button_image'])

    main_image = gobj.MainImage('main_image.png')
    gfw.world.add(gfw.layer.main_image, main_image)

    start_image = gobj.StartImage('start_image.png')
    gfw.world.add(gfw.layer.start_image, start_image)

    exit_image = gobj.ExitImage('exit_image.png')
    gfw.world.add(gfw.layer.exit_image, exit_image)

    button_image = gobj.ButtonImage('button_image.png')
    gfw.world.add(gfw.layer.button_image, button_image)

    global music_main, music_key, music_select
    music_main = load_wav('sound/main.wav')
    music_key = load_wav('sound/key.wav')
    music_select = load_wav('sound/select.wav')
    music_main.set_volume(30)
    music_main.repeat_play()

def update():
    gfw.world.update()
    global loading_on
    if loading_on:
        gfw.change(loading_state)
        loading_on = False
        gobj.effect1_on = False
        gobj.effect2_on = False

def draw():
    gfw.world.draw()

def handle_event(e):
    global button_image
    y = button_image.get_y()

    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.quit()
        elif e.key == SDLK_UP:
            music_key.play()
            if y == 300:
                button_image.set_y(200)
            elif y == 200:
                button_image.set_y(300)
        elif e.key == SDLK_DOWN:
            music_key.play()
            if y == 200:
                button_image.set_y(300)
            elif y == 300:
                button_image.set_y(200)
        elif e.key == SDLK_SPACE:
            music_select.play()
            delay(0.4)
            if y == 300:
                gobj.effect1_on = True
            elif y == 200:
                gobj.effect2_on = True
                gfw.quit()

def exit():
    global main_image, start_image, exit_image, button_image
    global music_main, music_key, music_select
    del main_image
    del start_image
    del exit_image
    del button_image
    del music_main
    del music_key
    del music_select

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()