import gobj
import gfw
import stage
from pico2d import *

# canvas_width = 600
# canvas_height = 800

def enter():
    global loading, first_image, second_image, third_image, fourth_image
    loading = gfw.image.load('res/player1_loading.png')
    first_image = gfw.image.load('res/loading1.png')
    second_image = gfw.image.load('res/loading2.png')
    third_image = gfw.image.load('res/loading3.png')
    fourth_image = gfw.image.load('res/loading4.png')

    global loading_time
    loading_time = 6

    global first_index, second_index, third_index, fourth_index
    first_index = 0
    second_index = 0
    third_index = 0
    fourth_index = 0

    global time
    time = 0

def update():
    global loading_time
    global first_index, second_index, third_index, fourth_index
    global time

    loading_time -= gfw.delta_time

    if loading_time < 6:
        if first_index < 7:
            time += 1
            if time % 5 == 1:
                first_index += 1

    if loading_time < 4.5:
        if second_index < 3:
            time += 1
            if time % 5 == 1:
                second_index += 1

    if loading_time < 3:
        if third_index < 3:
            time += 1
            if time % 5 == 1:
                third_index += 1

    if loading_time < 1.5:
        if fourth_index < 3:
            time += 1
            if time % 5 == 1:
                fourth_index += 1

    if loading_time <= 0:
        gfw.change(stage)

def draw():
    loading.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)
    global first_index, second_index, third_index, fourth_index

    if loading_time < 6:
        first_image.clip_draw(first_index * 123, 0, 123, 104, 150, 680, 185, 156)
    if loading_time < 4.5:
        second_image.clip_draw(second_index * 240, 0, 240, 104, 420, 530, 360, 156)
    if loading_time < 3:
        third_image.clip_draw(third_index * 240, 0, 240, 104, 150, 375, 360, 156)
    if loading_time < 1.5:
        fourth_image.clip_draw(fourth_index * 240, 0, 240, 104, 420, 215, 360, 156)


def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            pass

def exit():
    global loading
    gfw.image.unload('res/player1_loading.png')
    del loading

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()