import sys
import random
from pico2d import *

# 1000 명의 boy 가 생성된다.
# 초기에 로딩 하는 시간이 많이 걸린다.
# critical 한 문제가 잇다

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    # 객체들은 공유하는 동일한 변수를 갖게됨.
    image = None # 클래스 변수 ( C++ : static ) 모든 객체에 대해서 그 값은 유일하다.
    # 생성자 함수 : 객체를 생성할 때마다 실행이 된다.
    # 객체 멤버들이 갖는 초기값을 설정하는 용도이다.
    # 똑같은 내용으로 한번만 로드 하면 된다. 그래서 공유하게 만든다.

    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        # 단 한번의 리소스 로딩만 수행 : 이미지 리소스를 모든 객체가 공유
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame + 1) % 8
        # self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Boy() for i in range(1000)]


grass = Grass()

running = True;
while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()
