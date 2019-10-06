import lab5
from gfxhat import lcd, backlight
import time
import random

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
        lab5.getVertical()
    elif testnum == 2:
        lab5.getHorizontal()
    elif testnum == 3:
        lab5.getStaircase()
    elif testnum == 4:
        lab5.getDisplay()
    elif testnum == 5:
        lab5.clearBacklight()
    elif testnum > 5:
        break

