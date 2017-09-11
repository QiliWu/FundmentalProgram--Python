import turtle

def square_circle():
    window = turtle.Screen()
    window.bgcolor('yellow')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(5)
    brad.width(5)
    i = 0
    while i < 36:
        j=0
        while j < 4:
            brad.forward(100)
            brad.right(90)
            j=j+1
        brad.right(10)
        i=i+1

    window.exitonclick()

square_circle()
