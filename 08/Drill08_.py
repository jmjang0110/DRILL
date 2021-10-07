import math
import turtle
import random

KPU_WIDTH = 800
KPU_HEIGHT = 800


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    # 0 이 되는 경우를 해결 해야함
    # 기울기 계산
    # y = a*x + b
    a = (y2 - y1)/(x2 - x1)
    # y = ax + b ==> b = y - a * x
    b = y1 - a * x1


    for x in range(x1,x2+1,10):
        y = a * x + b
        draw_point((x,y))

    draw_point(p2) # 마지막점을 표현하기 위해서

    # a =
    # fill here
    pass


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 100+ 1, 2):
        t = i / 100
        x = (1-t) * x1 + t * x2
        y = (1-t) * y1 + t * y2
        draw_point((x,y))

    draw_point(p2)
    pass


def draw_curve_3_points(p1, p2, p3):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        draw_point((x, y))
    draw_point(p3)

    pass

def hypotrochoids1():
    global t
    t += 0.3
    a = 70
    b = 100
    d = 70

    # x = (a - b) * math.cos(t) + d * math.cos(((a - b)/b) * t)
    # y = (a - b) * math.sin(t) - d * math.sin(((a - b)/b) * t)
    x = (a - b) * math.cos(t) + d * math.cos(((a/b - 1) * t))
    y = (a - b) * math.sin(t) - d * math.sin(((a/b - 1) * t))


    print(x, y)

    draw_point((x, y))

def hypotrochoids2():
    global t2
    t2 += 0.3
    a = 140
    b = 100
    d = 200

    # x = (a - b) * math.cos(t) + d * math.cos(((a - b)/b) * t)
    # y = (a - b) * math.sin(t) - d * math.sin(((a - b)/b) * t)
    x = (a - b) * math.cos(t2) + d * math.cos(((a/b - 1) * t2))
    y = (a - b) * math.sin(t2) - d * math.sin(((a/b - 1) * t2))


    print(x, y)

    draw_point((x, y))


# 그리기를 시작합니다.
prepare_turtle_canvas()
t = 0.1
t2 = 0.1


p1 = (-300, 200)
p2 = (400, 350)
p3 = (300,-300)
p4 = (-200, -200)
# draw_line_basic(p1,p2)

# draw_line(p1,p2)
# fill here



while True:
    hypotrochoids1()
    hypotrochoids2()

turtle.done()