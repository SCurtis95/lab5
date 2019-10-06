import curt0061Library
from gfxhat import lcd, backlight
import time
import random

width, height = lcd.dimensions()

print("Welcome to the testing section")
print("Task 1: Creates a vertical Line on the GFXHat.")
print("Task 2: Creates a horizontal line on the the GFXHat.")
print("Task 3: Creates a staircase on the GFXHat")
print("Task 4: Displays a random pixel on the GFXHat")
print("Task 5: Resets the backlight color")

test = input("Please select a number between 1 and 5 to test a task or 0 to exit: ")
testnum = int(test)

while testnum > 0:
    if testnum == 1:
        curt0061Library.getVertical()
    elif testnum == 2:
        curt0061Library.getHorizontal()
    elif testnum == 3:
        curt0061Library.getStaircase(width, height)
    elif testnum == 4:
        curt0061Library.getDisplay()
    elif testnum == 5:
        curt0061Library.clearBacklight()
    elif testnum > 5:
        break

