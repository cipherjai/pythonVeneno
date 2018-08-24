class Line(object):
    """docstring for Line."""
    def __init__(self, coor1, coor2):
        super(Line, self).__init__()
        self.coordinate1 = coor1
        self.coordinate2 = coor2

    def distance(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return ((x2 - x1)**2 + (y2 - y1)**2 )**0.5

    def slope(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return float((y2 - y1)/(x2 - x1))

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder(object):
    """Docstring for Cylinder"""
    pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * self.radius ** 2

    def surface_area(self):
        top = 3.14 * self.radius ** 2
        return 2*top + (2*self.pi*self.radius*self.height)

