import gfw
import gobj
import collision
import main_state
import result_state
from pico2d import *
from player import Player
from enemy import Enemy
from item import Item
from boss import Boss

scoreX = 10
scoreY = 800 - 10
Color = (255, 255, 255)
score = 0
go_boss = 80

def enter():
    gfw.world.init(['stage_map', 'player', 'bullet', 'skill',
                    'enemy', 'enemy_bullet', 'item',
                    'boss', 'boss_bullet'])

    stage_map = gobj.StageMap('stage_map.png')
    gfw.world.add(gfw.layer.stage_map, stage_map)

    global player, player_life
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    player.end = False

    global boss
    boss = Boss()

    global enemy_time
    enemy_time = 2

    global item_gen_time
    item_gen_time = 1

    global stage_playtime
    stage_playtime = 0

    global score, font, life, pskill
    score = 0
    font = gfw.font.load('res/ENCR10B.TTF', 20)
    life = gfw.font.load('res/ENCR10B.TTF', 20)
    pskill = gfw.font.load('res/ENCR10B.TTF', 20)

    global music_stage, music_explosion, music_item
    music_stage = load_wav('sound/stage.wav')
    music_explosion = load_wav('sound/explosion.wav')
    music_item = load_wav('sound/item.wav')
    music_stage.set_volume(30)
    music_explosion.set_volume(30)

    music_stage.repeat_play()

def update():
    if player.end:
        result_state.IsWin = False
        gfw.change(result_state)
    gfw.world.update()

    global score
    score += gfw.delta_time

    # stage1 playetime
    global stage_playtime
    stage_playtime += gfw.delta_time

    # boss 출현
    if stage_playtime > go_boss:
        if gfw.world.count_at(gfw.layer.boss) == 0:
            gfw.world.add(gfw.layer.boss, boss)

    else:
        # enemy 생성 시간
        global enemy_time
        enemy_time -= gfw.delta_time
        if enemy_time <= 0:
            gfw.world.add(gfw.layer.enemy, Enemy())
            if stage_playtime >= 0 and stage_playtime < 20:
                enemy_time = 2
            elif stage_playtime >= 20 and stage_playtime < 40:
                enemy_time = 1.5
            else:
                enemy_time = 1

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_collision_enemy(e)

    for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
        check_collision_enemybullet(eb)

    for s in gfw.world.objects_at(gfw.layer.skill):
        check_collision_playerskill(s)

    # Item 생성
    global item_gen_time
    item_gen_time -= gfw.delta_time

    if item_gen_time <= 0:
        gfw.world.add(gfw.layer.item, Item())
        item_gen_time = 15

    check_collision_item()
    check_collision_boss()

def check_collision_enemy(e):
    # 충돌 enemy with player
    global player
    if not player.returninfo():
        if collision.collides_box(player, e):
            e.explosion()
            player.explosion()
            music_explosion.play(1)
            return

    # 충돌 enemy with player bullet
    for b in gfw.world.objects_at(gfw.layer.bullet):
        if collision.collides_box(b, e):
            e.explosion()
            music_explosion.play(1)
            b.remove()
            return

def check_collision_enemybullet(eb):
    # 충돌 enemy_bullet with player
    global player
    if not player.returninfo():
        if collision.collides_box(player, eb):
            player.explosion()
            music_explosion.play(1)
            return

def check_collision_playerskill(s):
    # 충돌 player skill with enemy
    for e in gfw.world.objects_at(gfw.layer.enemy):
        if collision.collides_box(s, e):
            e.explosion()
            music_explosion.play(1)
            return

    # 충돌 player skill with enemy_bullet
    for eb in gfw.world.objects_at(gfw.layer.enemy_bullet):
        if collision.collides_box(s, eb):
            eb.remove()
            return

def check_collision_item():
    # 충돌 player with item
    for i in gfw.world.objects_at(gfw.layer.item):
        if collision.collides_box(player, i):
            if player.upgrade < 4:
                player.upgrade += 1
            i.remove()
            music_item.play(1)
            return

def check_collision_boss():
    # 충돌 player with boss
    if collision.collides_box(player, boss):
        player.explosion()
        music_explosion.play(1)
        boss.hit = True

    # 충돌 player bullet with boss
    for b in gfw.world.objects_at(gfw.layer.bullet):
        if collision.collides_box(b, boss):
            b.remove()
            boss.hit = True
            # boss hp -
            boss.hp -= b.damage
            if boss.hp <= 0:
                boss.explosion()
                music_explosion.play(1)
            return

    # 충돌 player skill with boss
    for s in gfw.world.objects_at(gfw.layer.skill):
        if collision.collides_box(s, boss):
            # boss hp -
            boss.hit = True
            boss.hp -= s.damage
            if boss.hp <= 0:
                boss.explosion()
                music_explosion.play(1)
            return

    # 충돌 player with boss bullet
    for bb in gfw.world.objects_at(gfw.layer.boss_bullet):
        if collision.collides_box(player, bb):
            player.explosion()
            music_explosion.play(1)
            return

def draw():
    gfw.world.draw()

    global score, font, life, skill, player
    font.draw(scoreX, scoreY, "Score: %.2f" % score, Color)
    life.draw(500, 790, "Life: %d" % player.LIFE, Color)
    pskill.draw(500, 770, "Skill: %d" % player.skillcount, Color)

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.change(main_state)

    player.handle_event(e)

def get_playertime():
    global stage_playtime
    return stage_playtime

def exit():
    global music_stage, font, life, pskill
    del music_stage
    del font
    del life
    del pskill

if __name__=='__main__':
    gfw.run_main()