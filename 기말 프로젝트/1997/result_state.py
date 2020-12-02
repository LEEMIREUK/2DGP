import gfw
import main_state
import stage
import highscore
from pico2d import *

Color = (255, 255, 255)
IsWin = True

def enter():
    global bg, gameover, win, board, font
    bg = gfw.image.load('res/result_bg.png')
    gameover = gfw.image.load('res/game_over.png')
    board = gfw.image.load('res/board.png')
    win = gfw.image.load('res/win.png')

    highscore.load()
    highscore.add(stage.score)

    global music_gameover, music_win
    music_gameover = load_wav('sound/gameover.wav')
    music_gameover.set_volume(30)
    music_win = load_wav('sound/win.wav')
    music_win.set_volume(30)

    if IsWin:
        music_win.repeat_play()
    else:
        music_gameover.repeat_play()

def draw():
    bg.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)
    board.draw(get_canvas_width() // 2, get_canvas_height() // 2 - 100, 400, 400)
    if IsWin:
        win.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 200)
    else:
        gameover.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 200)

    highscore.draw()

def update():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(main_state)

def exit():
    global bg, gameover, board, music_gameover, music_win
    del bg
    del gameover
    del board
    del music_gameover
    del music_win