'''
class Example:
    x=100
    def display(self):
        print("This is a method of Example class")
obj= Example()
obj.display() 
print(obj.x)

#class circle with two methods - Area and perimeter
from math import pi
class Circle:
    r=7
    def Area(self):
        return pi *self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r
c=Circle()
print("Area:", c.Area())
print("Perimeter:", c.Perimeter())
'''