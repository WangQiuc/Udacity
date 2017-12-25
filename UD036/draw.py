import turtle

def draw():
    canvas = turtle.Screen()
    canvas.colormode(255)
    canvas.bgcolor(47, 85, 171)
    brush = turtle.Turtle()
    brush.setx(-300)
    brush.sety(300)
    brush.shape('turtle')
    brush.speed(6000)
    brush.color(240, 160, 80)
    for i in range (0, 72):
        for j in range (0, 2):
            brush.forward(100)
            brush.right(60)
            brush.forward(100)
            brush.right(120)
        brush.right(5)
    brush.right(90)
    brush.forward(500)



    canvas.exitonclick()

draw()
    
