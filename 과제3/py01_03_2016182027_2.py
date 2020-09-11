import turtle as t

def Move_To(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def Draw_Street(y):
    t.goto(500, y * 100)

def Draw_column(x):
    t.goto(x * 100, 500)

        
    
t.speed(0)  
Move_To(0, 0)
for i in range(6):
    Draw_Street(i)
    Move_To(0, (i+1)*100)
    
Move_To(0, 0)
for i in range(6):
    Draw_column(i)
    Move_To((i+1)*100, 0)

t.exitonclick()
