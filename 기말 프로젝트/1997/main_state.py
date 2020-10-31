from pico2d import *
import gfw
import gobj

canvas_width = 600
canvas_height = 800

def enter():
    global button_image
    open_canvas(canvas_width, canvas_height)
    gfw.world.init(['main_image', 'start_image', 'exit_image', 'button_image'])

    main_image = gobj.MainImage()
    gfw.world.add(gfw.layer.main_image, main_image)

    start_image = gobj.StartImage()
    gfw.world.add(gfw.layer.start_image, start_image)

    exit_image = gobj.ExitImage()
    gfw.world.add(gfw.layer.exit_image, exit_image)

    button_image = gobj.ButtonImage()
    gfw.world.add(gfw.layer.button_image, button_image)


def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    global button_image
    button_image.handle_event(e)

    if e.type == SDL_QUIT:
        gfw.quit()
    if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()

def exit():
    pass
    # global main_image, start_image, exit_image, button_image
    # del main_image, start_image, exit_image, button_image

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()