import gfw
import gobj
from pico2d import *
from player import Player
from bullet import Bullet

def enter():
    global player
    gfw.world.init(['stage1_map', 'player'])

    stage1_map = gobj.Stage1Map()
    gfw.world.add(gfw.layer.stage1_map, stage1_map)

    player = Player()
    gfw.world.add(gfw.layer.player, player)

def update():
    gfw.world.update()
    for b in Bullet.bullets:
        b.update()

def draw():
    gfw.world.draw()
    for b in Bullet.bullets:
        b.draw()

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()