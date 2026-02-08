# Python Code to Implement a Constructor in a Point class with Functions to Calculate Distance to Origin and Reflect the Point across an Axis

# Write the class Point as outlined in the instructions
import math
class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        if axis=="x":
            self.y = -self.y
        elif axis=="y":
            self.x = -self.x
        else:
            print("Invalid Choice")
