
import pygame as pg
from config import *
from obj import *

pg.font.init()


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("paint ( RMB to clear, right,left to switch adjust setting, A,D to adjust setting )")
screen.fill(fill)

clock = pg.time.Clock()

brush = Brush(screen)
status = Status(brush)



run = True

while run:


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                screen.fill(fill)

        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_RIGHT:            
                if brush.set == 3:
                    brush.set = 0
                else:
                    brush.set += 1

            elif event.key == pg.K_LEFT:
                if brush.set == 0:
                    brush.set = 3
                else:
                    brush.set -= 1
    
    
    brush.update()
    a = status.update()

    pg.draw.rect(screen, fill, (a[0][1][0]-10, a[0][1][1]-20, 230, 100), 0, 20)
    

    for i in a:
        screen.blit(i[0], i[1])

    pg.display.update()
    pg.display.flip()

    clock.tick(FPS)
