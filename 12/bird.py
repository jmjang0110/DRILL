import random

from pico2d import *
import game_world
import game_framework


from pico2d import *
import game_world
import game_framework


# R E A D M E
# 새의 속도 구현
# RUN_SPEED_KMPH = 20.0 # km / Hour 새의 움직이는 속도를 지정합니다.
# 이 변수를 통해서 새의 움직임 속도를 정했습니다.
# 속도는 시속 20km 로 지정했습니다.


# TIME_PER_ACTION = 0.5 # 새의 움직임 모션 속도를 지정합니다.
# 이 변수를 통해서 새의 움직임 모션 즉 새가 날갯짓하는 속도를 정했습니다.
# 이를 낮출 수록 새가 느리게 날갯짓합니다.

# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# 이 변수를 통해서 새가 시간당 움직임 정도를 설정하고
# self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
# 이를 game_framework.frame_time 과 곱해서 시간에 맞게 프레임이 지정되도록 설정했습니다.

# 새의 크기는
# 애니메이션 png 파일의 새 한마리의 크기가 100 100 이므로
# 이와 동일하게 100 100 으로 설정했습니다.



# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # km / Hour 새의 움직이는 속도를 지정합니다.
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = ( RUN_SPEED_MPM / 60.0 )
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# bird Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.6 # 새의 움직임 모션 속도를 지정합니다.
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5



class Bird:
    image = None

    def __init__(self, x = 400, y = 500, velocity = RUN_SPEED_PPS):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.y = random.randint(400,500)

        self.frame = 0
        self.dir = 0
        # self.Height_idx = 2

        self.Width = 100
        self.Height = 100
        # 새의 이동 시작 방향을 랜덤하게 설정합니다.
        if random.randint(1,2) == 1:
            self.velocity *= -1
        print(RUN_SPEED_KMPH)




    def draw(self):
        # 오른쪽
        if self.velocity >= 1:
            self.image.clip_draw(int(self.frame) * 100, 0, self.Width, self.Height, self.x, self.y)
        # 왼쪽
        else:
            self.image.clip_composite_draw(int(self.frame) * 100 ,0, self.Width, self.Height, 0.0, 'h', self.x, self.y,self.Width,self.Height)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14


        print('frame : ', self.frame)
        if self.x < 50 or self.x > 1600 - 50:
            self.velocity *= -1

        self.dir = clamp(-1, self.velocity, 1)






