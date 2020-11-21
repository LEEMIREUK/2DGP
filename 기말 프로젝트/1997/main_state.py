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
            if y == 300:
                button_image.set_y(200)
            elif y == 200:
                button_image.set_y(300)
        elif e.key == SDLK_DOWN:
            if y == 200:
                button_image.set_y(300)
            elif y == 300:
                button_image.set_y(200)
        elif e.key == SDLK_SPACE:
            if y == 300:
                gobj.effect1_on = True
            elif y == 200:
                gobj.effect2_on = True
                gfw.quit()

def exit():
    global main_image, start_image, exit_image, button_image
    del main_image
    del start_image
    del exit_image
    del button_image

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()