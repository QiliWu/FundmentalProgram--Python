import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('white')

    brad = turtle.Turtle()
    brad.width(5)
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(5)

    i = 0
    while i < 36:
        j = 0
        while j < 2:
            brad.forward(100)
            brad.right(60)
            brad.forward(100)
            brad.right(120)
            j += 1
        brad.right(10)
        i += 1
    brad.right(90)
    brad.forward(300)

    window.exitonclick()

draw_flower()