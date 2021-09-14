import turtle

def DrawMyInfo():
    turtle.penup()
    turtle.goto(-700,300)
    turtle.pendown()
    turtle.write(str("한국산업기술대학교 게임공학과 2018180035 장재문"))
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    
                 
def MoveUp():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def MoveDown():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def MoveLeft():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def MoveRight():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def Restart():
    turtle.reset()
    DrawMyInfo()
    

 
turtle.shape("turtle")
turtle.stamp()

turtle.onkey(DrawMyInfo,'q')
turtle.onkey(MoveUp,'w')
turtle.onkey(MoveDown,'s')
turtle.onkey(MoveLeft,'a')
turtle.onkey(MoveRight, 'd')
turtle.onkey(Restart,'Escape')

turtle.listen()



