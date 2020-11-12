import gfw
import gobj
from pico2d import *
from player import Player
from bullet import Bullet
from skill import Skill
from enemy import Enemy

def enter():
    global player
    gfw.world.init(['stage1_map', 'player', 'enemy', 'bullet', 'skill'])

    stage1_map = gobj.Stage1Map()
    gfw.world.add(gfw.layer.stage1_map, stage1_map)

    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global enemy_time
    enemy_time = 2

def update():
    gfw.world.update()

    global enemy_time
    enemy_time -= gfw.delta_time
    if enemy_time <= 0:
        gfw.world.add(gfw.layer.enemy, Enemy())
        enemy_time = 1

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

def check_enemy(e):
    if gobj.collides_box(player, e):
        e.explosion()
        player.explosion()
        return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            e.explosion()
            b.remove()
            return
    for s in gfw.gfw.world.objects_at(gfw.layer.skill):
        if gobj.collides_box(s, e):
            e.explosion()
            return

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

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