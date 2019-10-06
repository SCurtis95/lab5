def getVertical():
    
    x = 37
    for y in range(0,127,1):
        lcd.set_pixel(37,y,1)
    lcd.show()
    time.sleep(3)
    lcd.clear()


def getHorizontal():
    y = 68
    for x in range(0,63,1):
        lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(3)
    lcd.clear()
 

def getStaircase(width, height):
    x = 45
    y = 34
    lcd.set_pixel(x,y,1)
    for x in range (0,63):
        width = x + 1
        lcd.set_pixel(x,y,1)
        height = y + 1
        lcd.set_pixel(x,y,1)
    lcd.show() 

def getDisplay():
    x = random.randint(1,127)
    y = random.randint(1,63)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(4)
    lcd.clear()
    


def clearBacklight():
    lcd.clear()
    backlight.set_all(255,255, 255)
    time.sleep (2) 

