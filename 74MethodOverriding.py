'''Method Overriding in Python
Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method the version of the method in the derived class is executed rather than the version in the base class'''

class Shape:
    def __init__(self, x, y, z =1):
        self.x = x
        self.y = y
        self.z = z

    def area(self, ):
        return self.x * self.y * self.z
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)
    def area(self):
        # return 3.14 * self.radius**2 it was working stil....
        return 3.14 * super().area()
        
    
# rect = Shape(3,4)
# print(rect.area())
# circ1 = Circle(2)
# print(circ1.area())
circ = Circle(5)
print(circ.area())

    