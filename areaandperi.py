if __name__ == "__main__":

    import math
    from math import pi,sqrt
    from abc import abstractmethod
    from abc import ABCMeta
    #Abstarct Class
    class Shape(metaclass=ABCMeta):
        def area(self):
            pass
        def perimeter(self):
            pass

    class Circle(Shape):
        def __init__(self,radius):
            self.radius=radius

        def radius(self):
            return self.radius

        def area(self):
            return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def length(self):
        return self.length
    
    def breadth(self):
        return self.breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

class Triangle(Shape):
    def __init__(self,base,height,side_a,side_b,side_c):
        self.base=base
        self.height=height
        self.side_a=side_a
        self.side_b=side_b
        self.side_c=side_c

    def base(self):
        return self.base 

    def height(self):
        return self.height
    
    def side(self):
        return self.side

    def area(self):
        return 1/2*(float(self.base)*float(self.height))

    def perimeter(self):
        return self.side_a+self.side_b+self.side_c

class Diamond(Shape):
    def __init__(self,altitude,side):
        self.altitude=altitude
        self.side=side
        

        def altitude(self):
            return self.altitude

        def side1(self):
            return self.side

        def area(self):
            return self.altitude*self.side
        
        def perimeter(self):
            return self.side*4

