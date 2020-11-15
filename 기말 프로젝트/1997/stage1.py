import gfw
import gobj
import collision
from pico2d import *
from player import Player
from enemy import Enemy

def enter():
    global player
    gfw.world.init(['stage1_map', 'player', 'bullet', 'skill', 'enemy', 'enemy_bullet'])

    stage1_map = gobj.Stage1Map()
    gfw.world.add(gfw.layer.stage1_map, stage1_map)

    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global enemy_time
    enemy_time = 4

    global stage1_playtime
    stage1_playtime = 0

def update():
    gfw.world.update()

    global stage1_playtime
    stage1_playtime += gfw.delta_time

    global enemy_time
    enemy_time -= gfw.delta_time
    if enemy_time <= 0:
        gfw.world.add(gfw.layer.enemy, Enemy())
        if stage1_playtime >= 0 and stage1_playtime < 20:
            enemy_time = 2
        elif stage1_playtime >= 20 and stage1_playtime < 40:
            enemy_time = 1.5
        else:
            enemy_time = 1

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

def check_enemy(e):
    # 충돌 player with enemy
    if collision.collides_box(player, e):
        e.explosion()
        player.explosion()
        return

    # 충돌 player bullet with enemy
    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if collision.collides_box(b, e):
            e.explosion()
            b.remove()
            return

    # 충돌 player skill with enemy
    for s in gfw.gfw.world.objects_at(gfw.layer.skill):
        if collision.collides_box(s, e):
            e.explosion()
            return

    # 충돌 player with enemy_bullet
    for eb in gfw.gfw.world.objects_at(gfw.layer.enemy_bullet):
        if collision.collides_box(player, eb):
            player.explosion()
            return

def draw():
    gfw.world.draw()
    collision.draw_collision_box()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

    player.handle_event(e)

def get_playertime():
    global stage1_playtime
    return stage1_playtime

def exit():
    pass

if __name__=='__main__':
    gfw.run_main()