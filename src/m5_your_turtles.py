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
window = rg.TurtleWindow()

# turtles
blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue', 10)
blue_turtle.speed = 1 # Fast

pink_turtle = rg.SimpleTurtle('turtle')
pink_turtle.pen = rg.Pen('pink', 1)
pink_turtle.speed = 1  # Fast

# set turtles starting position
blue_turtle.pen_up()
blue_turtle.right(135)
blue_turtle.forward(400)
blue_turtle.right(135)
# The first square will be 300 x 300 pixels:
size = 200

# Do the indented code 13 times.  Each time draws a square.
for k in range(20):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.pen = rg.Pen('blue', 1+k)
    blue_turtle.speed = 2*k  # Fast
    blue_turtle.pen_down()
    blue_turtle.draw_square(-size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(size*.8)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size *= .8
window.close_on_mouse_click()