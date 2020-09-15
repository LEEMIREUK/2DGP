from pico2d import *

# pivot or origin

open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')

x = 0
while x <800:
    # render
    clear_canvas()
    gra.draw(400, 30)
    ch.draw(x, 85)
    update_canvas()

    # events
    get_events()

    # logic
    x+=2
    delay(0.01)


delay(1) # in seconds

close_canvas()
