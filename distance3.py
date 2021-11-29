
import math

#1. Class Defination
class Distance():
    #1. Property

    #2. Constructor

    #.3 Method
    def calculateDistance(anil,x1,x2,y1,y2):
        x = x1-x2
        x = x*x
        y = y1 - y2
        y = y*y
        return math.sqrt(x+y)

#2. Lets Create a Class Object

myobject = Distance()

#now call the calculateDistance method and

result = myobject.calculateDistance(3,7,2,8)

print(f'The distance between two points is {result}')
