"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jacob Oblazny.
"""
########################################################################
# TODO: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
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
import math
sqrt2 = math.sqrt(2)
degree = 30
window = rg.TurtleWindow()

# construct turtles
blue_turtle = rg.SimpleTurtle('turtle')
pink_turtle = rg.SimpleTurtle('turtle')

# set turtles starting position
degrees_right = 45
reset_degrees = 180 + degrees_right
length_forward = 200
blue_turtle.pen_up()
blue_turtle.right(degrees_right)
blue_turtle.forward(length_forward)
blue_turtle.right(reset_degrees)

pink_turtle.pen_up()
pink_turtle.right(degrees_right)
pink_turtle.forward(length_forward)
pink_turtle.right(reset_degrees + degree)
# The first square will be 300 x 300 pixels:
size = 244

# Do the indented code 13 times.  Each time draws a square.
for k in range(13):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.pen = rg.Pen('blue', 13*(1/(1+k)))
    blue_turtle.speed = 2*k  # Fast
    blue_turtle.pen_down()
    blue_turtle.left(degree)
    blue_turtle.draw_square(size)

    pink_turtle.pen = rg.Pen('pink', 13 * (1 / (1 + k)))
    pink_turtle.speed = 2 * k  # Fast
    pink_turtle.pen_down()
    pink_turtle.left(degree)
    pink_turtle.forward(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(degree)
    blue_turtle.forward(size)
    blue_turtle.left(degree)



    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size /= sqrt2
window.close_on_mouse_click()