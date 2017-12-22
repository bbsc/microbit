# <-- This is a comment.
#     Anything written after a # is ignored by the computer.
#     Things writen in comments can help the person reading
#     the code to understand it, so comments are generally a
#     a good thing to have in your code.

# This import statement is needed to accesss all the functions
# in the microbit module. In python, modules are a way of grouping
# related functions and other code under a single name. Here the *
# character is a "wildcard" meaning import everything within the
# microbit module into our program.
from microbit import *

# After our import statemet, we are able to now call fcuntions such
# as display.set_pixel(1, 1, 9) to turn on an LED on the microbit.
# Here, we are calling the function display.set_pixel arguments
# "0, 1, 9". The first argument 0 indicates column 0 on the mirobit,
# 1 is row 1, and 9 is the brightness.
display.set_pixel(0, 0, 9)

# This is a while loop. Because we say while True:, this means run the
# block of indented code below forever until a break statement is
# called.
while True:
    # Here, we call three statements if button a (the left button) is
    # pressed.
    if button_a.get_presses() > 0:
        # Set led at position 0, 0 to brightness 0 (turn if off)
        display.set_pixel(0, 0, 0)
        # Do nothing for 1000 milliseconds
        sleep(1000)
        # Break out of the while loop
        break

# This is a for loop. Notice how it ends is a : character. Every line
# that is indented after the for line is part of a block of code that runs
# for each iteration of the for statement. 
for x in [0, 1, 2, 3, 4]:
    y = 0
    # Light up pixel in grid position indicated at brightness level 9
    display.set_pixel(x, y, 9)
    # Here we print to the repl window (click the "Repl" button in mu)
    print('Turning on pixel in column {X}'.format(X=x))
    # Do nothing for 1000 milliseconds (1 second)
    sleep(1000)
