import math

#1. Function Defination
def distance(x1,x2,y1,y2):
    x = x1-x2
    x = x*x
    y = y1 - y2
    y = y*y
    return math.sqrt(x+y) # Fruitful Functions

#2. Function Calling
result = distance(3,7,2,8)
print(f"The distance between two given points is { result }")

