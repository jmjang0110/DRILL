from pico2d import *
import random


# 행위 : 객체의 상태를 바꾸어 주는 것
# 추상화 : 속성 + 행위 = 객체 지향
# class : 객체를 찍어내는 도장
# object instantiation  : 객체 생성
# instance : 생성된 각각의 객체

# Game object class here
class Grass:
    # 생성자
    def __init__(self):
        self.image = load_image('grass.png')

    # 객체를 그립니다.
    def draw(self):
        self.image.draw(400, 30)

    pass


class Ball:
    def __init__(self):
        self.image_SmallBall = load_image('ball21x21.png')
        self.image_BigBall = load_image('ball41x41.png')
        self.BigSize = 80
        self.SmallSize = 40

        self.x, self.y = random.randint(10, 700), 599
        self.speed = random.randint(2,8)
        self.collect_Size = random.randint(1,10) % 2

    def update(self):
        self.y -= self.speed
        if self.y <= 90:
            self.y = 90

    def draw(self):
        if self.collect_Size == 1:
            self.image_BigBall.clip_draw(0, 0, self.BigSize, self.BigSize , self.x, self.y)
        elif self.collect_Size == 0:
            self.image_SmallBall.clip_draw(0 ,0,  self.SmallSize ,  self.SmallSize , self.x, self.y)


# class SmallBall:
#     def __init__(self):
#         self.image_SmallBall = load_image('ball21x21.png')
#         self.image_BigBall = load_image('ball41x41.png')
#         self.Size = 80
#         self.SmallSize = 40
#
#         self.x, self.y = random.randint(10, 700), 599
#         self.speed = random.randint(5, 10)
#         self.collect_Size = random.randint(1, 10) % 2
#
#     def update(self):
#         self.y -= self.speed
#         if self.y <= 90:
#             self.y = 90
#
#     def draw(self):
#         if self.collect_Size == 1:
#             self.image_BigBall.clip_draw(0, 0, self.BigSize, 80, self.x, self.y)
#         elif self.collect_Size == 0:
#             self.image_SmallBall.clip_draw(0, 0, 50, 50, self.x, self.y)



class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(50, 400), 90
        self.frame = random.randint(0,7)

    #  소년의 행위 구현
    def update(self):
        # 속성 값을 바꿈으로 오른쪽으로 이동
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100 , 0, 100 , 100 , self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
# team
team = [Boy() for i in range(11)]
# Ball team
Balls = [Ball() for a in range(21)]


# boy = Boy()

# game main loop code

# 초기화 - 게임로직(객체 상호작용) - 그리기 (Rendering)
# - 종료 : game framework

running = True

def Update_All():
    global team
    global Balls

    for boy in team:
        boy.update()
    for Ball in Balls:
        Ball.update()

def Render_All():
    global Balls
    global team

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in Balls:
        ball.draw()

    update_canvas()

while running :
    handle_events()
#     game Logic
    Update_All()
#     game Rendering
    Render_All()
    delay(0.05)
# finalization code
# 파이썬은 del 하지 않아도 객체를 알아서 삭제해준다.
