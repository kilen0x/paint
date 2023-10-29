import pygame as pg
from config import *

pg.font.init()

class Brush:
    def __init__(self, screen = None, width = 20, color = [100,100,100]):
        self.color = color
        self.width = width
        self.screen = screen
        self.set = 0
        self.maxwidth = 100

    def update(self):
        ## change ##
        
        if pg.key.get_pressed()[pg.K_d]:
            if self.set != 3:
                v = self.color[self.set]
                if v == 255:
                    v = 0
                else:
                    v += 1

                self.color[self.set] = v
            else:
                if self.width > self.maxwidth:
                    self.width = 0
                else:
                    self.width += 1

        elif pg.key.get_pressed()[pg.K_a]:
            if self.set != 3:
                v = self.color[self.set]
                if v == 0:
                    v = 255
                else:
                    v -= 1

                self.color[self.set] = v
            else:
                if self.width == 0:
                    self.width = self.maxwidth
                else:
                    self.width -= 1

        if pg.mouse.get_pressed()[0]:
            ## draw ##
            pos = pg.mouse.get_pos()

            
            pg.draw.circle(self.screen, self.color, pos, self.width)
            pg.display.update()

class Status:
    def __init__(self, brush:Brush):
        self.screen = brush.screen
        self.brush = brush
        self.font = pg.font.Font(None, 50) ## 
        self.textcolor = (255,255,255)

        ## pos ##

        self.text1pos = (30, 10)
        self.text2pos = (30, 50)
        self.rectpos = (280, 1, 50, 50)

    def update(self):

        t1 = self.font.render(f"{self.brush.color[0]}, {self.brush.color[1]}, {self.brush.color[2]}", True, self.textcolor)
        t2 = self.font.render(f"Width: {self.brush.width}", True, self.textcolor)
        rect = pg.draw.rect(self.screen, self.brush.color, self.rectpos)
        
        return [[t1, self.text1pos], [t2, self.text2pos]]


