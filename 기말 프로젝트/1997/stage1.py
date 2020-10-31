from pico2d import *
import gfw
import main_state
import gobj

def enter():
    gfw.world.init(['stage1_map'])

    stage1_map = gobj.Stage1Map()
    gfw.world.add(gfw.layer.stage1_map, stage1_map)

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()