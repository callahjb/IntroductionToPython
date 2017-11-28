"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joseph Callahan.
"""
########################################################################
# done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOU WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
black_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)
black_turtle.pen = rg.Pen('black', 3)
red_turtle.speed = 100  # Fast
black_turtle.speed = 100

# The first square will be 300 x 300 pixels:
size = 1.01

# Do the indented code 13 times.  Each time draws a square.
for k in range(12):

    # Put the pen down, then draw a square of the given size:
    red_turtle.draw_circle(size)
    black_turtle.draw_circle(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    red_turtle.pen_up()
    red_turtle.right(45)
    red_turtle.forward(10)
    red_turtle.left(45)

    black_turtle.pen_down()
    black_turtle.left(45)
    black_turtle.backward(10)
    black_turtle.right(45)


    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    red_turtle.pen_down()
    black_turtle.pen_down()

    size = size*2

for k in range(20):

    # Put the pen down, then draw a square of the given size:
    red_turtle.draw_circle(size)
    black_turtle.draw_circle(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    red_turtle.pen_up()
    red_turtle.right(45)
    red_turtle.forward(10)
    red_turtle.left(45)

    black_turtle.pen_down()
    black_turtle.left(45)
    black_turtle.backward(10)
    black_turtle.right(45)


    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    red_turtle.pen_down()
    black_turtle.pen_down()

    size = size*.5

window.close_on_mouse_click()
