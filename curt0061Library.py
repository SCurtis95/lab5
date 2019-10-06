
def calculateAreaOfCircle():
    import math
    radius = input("Please enter a radius: ")

    radiusInt = int(radius)

    areaOfCircle = (math.pi * radiusInt ** 2)

    aoC = str(areaOfCircle)

    calcmpg = print("The area of the circle is " + aoC)
    return calcmpg



def calculateMPG():
    miles = input("Please enter in the number of miles you have driven: ")
    gas = input("Now, in gallons, enter in how much gas you have used: ")

    milesInt = int(miles)
    gasInt = int(gas)

    mpgInt = (milesInt / gasInt)
    mpg = str(mpgInt)

    print("You have been driving " + mpg + " miles per gallon")



def convertFahrenheitToCelsius():
    temp = input("Please enter in the degrees in fahrenheit: ")

    fahTemp = int(temp)

    celsius = ((fahTemp - 32) / 1.8)
    cel = round(celsius)
    finalTemp = str(cel)

    print("The temprature " + temp + " in fahrenheit is " + finalTemp + " degrees in celsius")


def calcDistance(x,x1,y,y1):
    
    import math
    points = math.sqrt((x1 - x)**2 + (y1 - y)**2)
    dist = int(points)
    calc = print("The total distance between points is : ", dist)
    return calc
