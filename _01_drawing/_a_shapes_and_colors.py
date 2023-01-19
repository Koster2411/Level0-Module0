import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    turtle_ = turtle.Turtle()


    # Make your turtle's shape 'turtle', .shape('turtle')
    turtle_.shape('turtle')
    # Set your turtle's speed using .speed(2)
    turtle_.speed(10)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    turtle_.color('blue')
    turtle_.pencolor('green')
    turtle_.goto(0,0)
    # Move your turtle forward using .forward(100)
    for i in range(100):
        turtle_.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
        turtle_.left(2)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    #yes

    # Move your turtle to a new place on the screen using .goto(x, y)
        turtle_.goto(0,0)

    # x=0 and y=0 is the center of the screen
        turtle_.goto(0,-10)
        turtle_.circle(50, steps=30)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
