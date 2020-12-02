import gfw
import main_state
import stage
import highscore
from pico2d import *

Color = (255, 255, 255)

def enter():
    global bg, gameover, board, font
    bg = gfw.image.load('res/result_bg.png')
    gameover = gfw.image.load('res/game_over.png')
    board = gfw.image.load('res/board.png')
    # save_score()
    # load_score()

    highscore.load()
    highscore.add(stage.score)

    global music_result
    music_result = load_wav('sound/result.wav')
    music_result.set_volume(30)
    music_result.repeat_play()

def draw():
    bg.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)
    gameover.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 200)
    board.draw(get_canvas_width() // 2, get_canvas_height() // 2 - 100)

    highscore.draw()

def update():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(main_state)

# def save_score():
#     file = []
#     with open('data.json', 'r') as f:
#         files = json.load(f)
#     for z in files:
#         file.append(z)
#     data = [float(stage.score)]
#     file.append(data)
#     with open('data.json', 'w') as f:
#         json.dump(file, f)
#
# def load_score():
#     global score
#     with open('data.json', 'r') as f:
#         score = json.load(f)
#     score.sort(reverse=True)

def exit():
    global bg, gameover, board, font, music_result
    del bg
    del gameover
    del board
    #del font
    del music_result