from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here


def Move_Rect(x,y):
    while True:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        
        if y == 90:
            if x < 780:
                x += 2

        if x >= 780 :
            if y < 580:
                x = 780
                y += 2
        
        if y >= 580:
           x -= 2
           y = 580

        if x <= 20 :
            y -= 2
            x = 20

        if x >= 380:
            if x < 400:
                if y == 90:
                    return True
        delay(0.01)
           
        
      
    

def Move_Circle(x,y, time):
    while True:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        time += 0.01
        x = 400 + math.cos(time) * 200 
        y = 300 + math.sin(time) * 200
        if time == 10:
            return True

    


#def Game_Rendering(x,y):
    
   



x= 400
y = 90
start = True
end = False
start2 = True
end2 = False

while end2 == False:
    clear_canvas_now()
    if start == True:
        end = Move_Rect(x,y)
        if end == True:
            start = False
    
    if start == False:
        if end2 == False:
            end2 = Move_Circle(400,90,0.0)

    if end2 == True:
        end2 = False
        end = False
        


    
close_canvas()
