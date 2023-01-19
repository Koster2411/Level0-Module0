import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    turtle_ = turtle.Turtle()
    # This code sets our shape to a turtle
    turtle_.shape('arrow')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    turtle_.speed(5)
    # Set your turtle's color using .color('green')
    turtle_.color('green')
    turtle_.pensize(3)
    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        # Set the turtle color to a random color
        turtle_.color(get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        turtle_.forward(4*i)
        # Turn the turtle (360/7) degrees to the right
        turtle_.right(360/3)
        # Change the turtle width to 'i' (the loop variable)
        turtle_.shapesize(1)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
