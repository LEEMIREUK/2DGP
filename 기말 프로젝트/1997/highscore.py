import pickle
import gfw
from pico2d import *

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 5
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score

def load():
    global font
    font = gfw.font.load('res/ENCR10B.TTF', 30)

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_score
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_score = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_score = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_score <= MAX_SCORE_COUNT:
        save()

def draw():
    global font, last_score
    no = 1
    x = get_canvas_width() // 2 - 200
    y = get_canvas_height() // 2 + 100
    for e in scores:
        str = "{:2d} {:7.1f}".format(no, e.score)
        color = (255, 255, 255) if no == last_score else (150, 240, 170)
        font.draw(x, y, str, color)
        y -= 30
        no += 1

def update():
    pass