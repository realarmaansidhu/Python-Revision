# LSP states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. In other words, if class B is a subclass of class A, then we should be able to use an object of class B wherever an object of class A is expected without causing any issues.

# Python Code to dempomnstrate the Rectangle-Square problem which violates the Liskov Substitution Principle

class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h
      
# Define set_h to set h       
    def set_h(self, h):
      self.h = h

# Define set_w to set w
    def set_w(self, w):
      self.w = w   
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 
      
# Define set_h to set w and h 
    def set_h(self, h):
      self.h = h
      self.w = h
      
# Define set_w to set w and h 
    def set_w(self, w):
      self.w = w   
      self.h = w  