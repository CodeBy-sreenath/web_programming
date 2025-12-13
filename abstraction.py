from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r
obj=Rectangle(3,4)
print(obj.area())
obj1=Circle(3)
print(obj1.area())                    