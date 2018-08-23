# methods

class Circle(object):
    """docstring for Circle."""
    # def __init__(self, arg):
    #     super(Circle, self).__init__()
    #     self.arg = arg

    # class object attributes
    # something that is true for all the instance of this object class
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius


    def area(self):
        # r ** 2 * pi
        return (self.radius**2) * Circle.pi

    def perim(self):
        # 2 * pi * r
        return 2 * self.pi * self.radius

    def setRadius(self, new_radius):
        # setting local radius
        self.radius = new_radius


    def getRadius(self):
        #get the radius
        return self.radius


c = Circle(radius = 100)
print(c.radius)
print(c.pi)
print(Circle.pi)
print(c.area())

c.setRadius(200)
print(c.getRadius())
print(c.perim())
