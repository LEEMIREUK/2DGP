import gfw
import stage
from pico2d import *

def enter():
    global loading, first_image, second_image, third_image, fourth_image
    loading = gfw.image.load('res/player1_loading.png')
    first_image = gfw.image.load('res/loading1.png')
    second_image = gfw.image.load('res/loading2.png')
    third_image = gfw.image.load('res/loading3.png')
    fourth_image = gfw.image.load('res/loading4.png')

    global loading_time
    loading_time = 4

    global first_index, second_index, third_index, fourth_index
    first_index = 0
    second_index = 0
    third_index = 0
    fourth_index = 0

    global time
    time = 0

    global music_loading
    music_loading = load_wav('sound/loading.wav')
    music_loading.set_volume(30)
    music_loading.play(1)

def update():
    global loading_time
    global first_index, second_index, third_index, fourth_index
    global time

    loading_time -= gfw.delta_time

    if loading_time < 4:
        if first_index < 7:
            time += 1
            if time % 5 == 1:
                first_index += 1

    if loading_time < 3:
        if second_index < 3:
            time += 1
            if time % 5 == 1:
                second_index += 1

    if loading_time < 2:
        if third_index < 3:
            time += 1
            if time % 5 == 1:
                third_index += 1

    if loading_time < 1:
        if fourth_index < 3:
            time += 1
            if time % 5 == 1:
                fourth_index += 1

    if loading_time <= 0:
        gfw.change(stage)

def draw():
    loading.draw(get_canvas_width() // 2, get_canvas_height() // 2, 600, 800)
    global first_index, second_index, third_index, fourth_index

    if loading_time < 4:
        first_image.clip_draw(first_index * 123, 0, 123, 104, 150, 680, 185, 156)
    if loading_time < 3:
        second_image.clip_draw(second_index * 240, 0, 240, 104, 420, 530, 360, 156)
    if loading_time < 2:
        third_image.clip_draw(third_index * 240, 0, 240, 104, 180, 375, 360, 156)
    if loading_time < 1:
        fourth_image.clip_draw(fourth_index * 240, 0, 240, 104, 420, 215, 360, 156)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            pass

def exit():
    global loading, first_image, second_image, third_image, fourth_image
    global music_loading
    del loading
    del first_image
    del second_image
    del third_image
    del fourth_image
    del music_loading

def pause():
    pass

if __name__ == '__main__':
    gfw.run_main()