import turtle as t

def Move_To(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def Draw_ieung():
    t.circle(35)


def Draw_mieum():
    for i in range(4):
        t.forward(55)
        t.left(90)

    
def Draw_rieul():
    t.forward(70)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(70)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(70)

def Draw_giyeok():
    t.forward(70)
    t.right(90)
    t.forward(30)

def Draw_eu():
    t.forward(110)

def Draw_e():
    t.right(90)
    t.forward(100)
    t.left(90)
     

t.shape('turtle')
t.speed(0)

Move_To(-200, 0)
Draw_ieung()
Move_To(-140, 90)
Draw_e()
Move_To(-80, 10)
Draw_mieum()
Move_To(10, 90)
Draw_e()
Move_To(80, 90)
Draw_rieul()
Move_To(60, 40)
Draw_eu();
Move_To(80, 30)
Draw_giyeok()

t.exitonclick()
