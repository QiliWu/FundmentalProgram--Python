import turtle

def draw_square():
    window = turtle.Screen() #set window as the screen for turtle
    window.bgcolor('red')     # set the screen color as red

    brad = turtle.Turtle()    # Call the function of turtle, name it as brad
    brad.shape('turtle')    # set the shape of brad
    brad.color('green')     #set the color of the brad
    brad.speed(2)           #set the move speed of the brad, num in the ()
    step = 0
    while step < 4:
        brad.forward(100)  # move 100 steps forward
        brad.right(90)     # turn 90 degree right
        step +=1

    angie = turtle.Turtle() # the second paintbrush name angie
    angie.shape('circle')
    angie.color('blue')
    angie.speed(1)
    angie.circle(100)   # draw a circle with radius of 100

    window.exitonclick()    # exit the window after click

draw_square()

