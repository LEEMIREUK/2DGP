from pico2d import *

open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')

gra.draw_now(400, 30)
ch.draw_now(400, 85)

delay(2)

close_canvas()
