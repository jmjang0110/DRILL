import math

from pico2d import *
import random
from enum import Enum

open_canvas()
KPU_Ground = load_image("KPU_GROUND.png")
Character = load_image("animation_sheet.png")
Hand_Arrow = load_image("hand_arrow.png")
KPU_HEIGHT = 600
KPU_WIDTH = 800
hide_cursor()

class Direction(Enum):
    STOP = 0
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    JUMP = 5



class MyMouse:
    def __init__(self,x,y):
        self.MyX = x
        self.MyY = y

    def UpdateMouse2Pico2d(self, WindowX, WindowY):
        self.MyX = WindowX
        self.MyY = KPU_HEIGHT - 1 - WindowY

    def Render(self):
        Hand_Arrow.clip_draw(0,0,50,50, self.MyX, self.MyY)


class MyCharacter:
    def __init__(self,x,y,Speed,Size, MyDirection):
        self.MyX = x
        self.MyY = y
        self.Size = Size
        self.Speed = Speed
        self.MyDirection = MyDirection
        self.PrevDirection = MyDirection
        self.V_Move2Mouse = {'x': 0.01, 'y': 0.01}

    def UpdateVector2Mouse(self):
        global Mouse

        self.V_Move2Mouse['x'] = Mouse.MyX - self.MyX
        self.V_Move2Mouse['y'] = Mouse.MyY - self.MyY

    def Move2Mouse(self):
        global Mouse
        global Reach2Mouse
        self.MyX += self.V_Move2Mouse['x'] // 50 * 0.05
        self.MyY += self.V_Move2Mouse['y'] // 50 * 0.05
        # if self.MyX != Mouse.MyX and self.MyY != Mouse.MyY:
        #     self.MyX += self.V_Move2Mouse['x'] // 50 * 0.25
        #     self.MyY += self.V_Move2Mouse['y'] // 50 * 0.25


        if Mouse.MyX - self.Size * 1.3<= self.MyX and self.MyX <= Mouse.MyX + self.Size * 1.3:
            if Mouse.MyY - self.Size * 1.3 <= self.MyY and self.MyY <= Mouse.MyY + self.Size * 1.3:
                Reach2Mouse = True
        # if self.MyX - self.Size * 2 <= Mouse.MyX and Mouse.MyX <= self.MyY + self.Size * 2:
        #     if self.MyY - self.Size * 2 <= Mouse.MyY and Mouse.MyY <= self.MyY + self.Size * 2:
        #         Reach2Mouse = True
        # elif Mouse.MyX - self.Size * 2.2 <= self.MyX and self.MyX <= Mouse.MyX + self.Size * 2.2:
        #     if Mouse.MyY - self.Size * 2.2 <= self.MyY and self.MyY <= Mouse.MyY + self.Size * 2.2:
        #         Reach2Mouse = True
        else :
            self.MyX += self.V_Move2Mouse['x'] // 50 * 0.3
            self.MyY += self.V_Move2Mouse['y'] // 50 * 0.3


            Reach2Mouse = False




    def Move2Mouse_Render(self, frame):
        global Mouse

        Angle = math.atan2(Mouse.MyY - self.MyY, Mouse.MyX - self.MyX)
        degree = Angle * 180 / math.pi
        if degree >= 0 :
            Character.clip_composite_draw(frame * 100,100,100,100, Angle, 'd', self.MyX, self.MyY, 100 , 100)
        elif degree < 0:
            Character.clip_composite_draw(frame * 100, 100, 100, 100, Angle, 'd', self.MyX, self.MyY, 100, 100)


def Hand_events():

    global bRun
    global Mouse

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            bRun = False
        # if event.type == SDL_MOUSEMOTION:
        #     Mouse.UpdateMouse2Pico2d(event.x, event.y)



bRun = True
Mouse = MyMouse(random.randrange(1,KPU_WIDTH), random.randrange(1,KPU_HEIGHT))
frame = 0
Mario = MyCharacter(KPU_WIDTH // 2,KPU_HEIGHT // 2, 0.5 ,50, Direction.RIGHT)

Reach2Mouse = False
Mario.UpdateVector2Mouse()

while bRun:
    clear_canvas()
    frame = (frame + 1) % 8
    Hand_events()

    if Reach2Mouse == True:
        Mouse.UpdateMouse2Pico2d(random.randrange(1,KPU_WIDTH), random.randrange(1,KPU_HEIGHT))
        Mario.UpdateVector2Mouse()



    KPU_Ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Mario.Move2Mouse()
    Mouse.Render()
    Mario.Move2Mouse_Render(frame)

    update_canvas()