class Figure:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def triangle_area(self):
        return (self.a * self.b) / 2


class MoreFigures(Figure):
    def __init__(self, a, b, c):
        #super() will make class inherit all the methods and props from parent
        super().__init__(a, b)
        self.c = c

    def polygon_area(self):
        return self.a * self.c


polygon = MoreFigures(12,13,23)
polygon_area = polygon.polygon_area()
print(polygon_area)
triangle = Figure(12,13)
print(triangle.triangle_area())