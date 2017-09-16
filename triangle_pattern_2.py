import turtle

def single_triangle(some_turtle):
    some_turtle.fillcolor('green')  #  move the filling code from draw_triangle_pattern, fill the triangle one by one

    some_turtle.begin_fill()  # start color fill , just before starting drawing

    for j in range(3):
        some_turtle.forward(30)
        some_turtle.left(120)

    some_turtle.end_fill()  # end color fill when the drawing finished



def nine_triangles(some_turtle):
    #line one
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.left(120)
    some_turtle.pendown()
    #line two
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.forward(30)
    some_turtle.pendown()
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.backward(30)
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.left(120)
    some_turtle.pendown()
    #line three
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.forward(60)
    some_turtle.pendown()
    single_triangle(some_turtle)
    some_turtle.penup()
    some_turtle.backward(60)
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.left(120)
    some_turtle.pendown()
    #line four
    for i in range(3):
        single_triangle(some_turtle)
        some_turtle.penup()
        some_turtle.forward(30)
        some_turtle.pendown()
    single_triangle(some_turtle)

def triangle_pattern(some_turtle):
    nine_triangles(some_turtle)
    some_turtle.penup()
    some_turtle.backward(90)
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.left(120)
    some_turtle.pendown()
    nine_triangles(some_turtle)
    some_turtle.penup()
    some_turtle.forward(30)
    some_turtle.left(60)
    some_turtle.forward(90)
    some_turtle.right(60)
    some_turtle.pendown()
    nine_triangles(some_turtle)

def draw_triangle_pattern():
    window = turtle.Screen()
    window.bgcolor('white')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(5)
    brad.width(2)

    triangle_pattern(brad)

    window.exitonclick()


draw_triangle_pattern()







