import gfw
import main_state
import stage
from pico2d import *
Color = (255, 255, 255)

def enter():
    global bg, gameover, board, font
    bg = gfw.image.load('res/result_bg.png')
    gameover = gfw.image.load('res/game_over.png')
    board = gfw.image.load('res/board.png')
    font = gfw.font.load('res/ENCR10B.TTF', 20)
    save_score()
    load_score()

def draw():
    bg.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)
    gameover.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 200)
    board.draw(get_canvas_width() // 2, get_canvas_height() // 2 - 100)

    font.draw(225, 400, 'Score: %.2f' % stage.score, Color)
    # font.draw(225, 300, 'High Score: %.2f' % )

def update():
    pass

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.change(main_state)

def save_score():
    file = []
    with open('data.json', 'r') as f:
        files = json.load(f)
    for z in files:
        file.append(z)
    data = [float(stage.score)]
    file.append(data)
    with open('data.json', 'w') as f:
        json.dump(file, f)

def load_score():
    global score
    with open('data.json', 'r') as f:
        score = json.load(f)
    score.sort(reverse=True)

def exit():
    global bg, gameover, board, font
    del bg
    del gameover
    del board
    del font