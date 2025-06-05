from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
window.fill((210, 255, 255))
clock = time.Clock()
FPS = 60

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)