import turtle

count = 5
length = 500
size = 100
startx = -300
starty = -300

turtle.penup()
turtle.goto(startx, starty)
turtle.pendown()

while(count >= 0):
    turtle.forward(length)
    starty = starty + size
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.pendown()
    count -= 1

turtle.penup()
startx = -300
starty = 200
turtle.goto(startx,starty)
turtle.right(90)
turtle.pendown()

count = 5
while(count >= 0):
    turtle.forward(length)
    startx = startx + size
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    count -= 1

turtle,penup()
turtle.goto(-300,200)
turtle.pendown()

turtle.exitonclick()

