import turtle


def single_triangle(some_turtle):
    for j in range(3):
        some_turtle.forward(30)
        some_turtle.left(120)
   # when the circle finished, the turtle will turn back to its initial direction automatically


def three_triangle(some_turtle):
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.forward(30)
    some_turtle.pendown()
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.left(120)    #after this, the turtle keep the final direction
    some_turtle.forward(30)
    some_turtle.right(120)
    some_turtle.pendown()
    single_triangle(some_turtle)


def triangle_pattern(some_turtle):
    three_triangle(some_turtle)
    for i in range(3):
        some_turtle.penup()
        some_turtle.left(60)
        some_turtle.forward(30)
        some_turtle.right(60)
        some_turtle.pendown()
        three_triangle(some_turtle)
    for j in range(3):
        some_turtle.penup()
        some_turtle.right(120)
        some_turtle.forward(30)
        some_turtle.left(60)
        some_turtle.forward(60)
        some_turtle.left(60)
        some_turtle.pendown()
        three_triangle(some_turtle)
    for k in range(2):
        some_turtle.penup()
        some_turtle.backward(60)
        some_turtle.right(120)
        some_turtle.forward(30)
        some_turtle.left(120)
        some_turtle.pendown()
        three_triangle(some_turtle)
    some_turtle.penup()

def draw_triangle_pattern():
    window = turtle.Screen()
    window.bgcolor('white')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(5)
    brad.width(2)

    brad.fillcolor('green')   #
    brad.begin_fill()  # start color fill , just before starting drawing

    triangle_pattern(brad)






    brad.end_fill()   # end color fill when the drawing finished

    window.exitonclick()

draw_triangle_pattern()

# the result has an error in fill