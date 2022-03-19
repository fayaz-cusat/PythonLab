import math


class ThreeDShape:
    def printVolume():
        raise NotImplementedError

    def printArea():
        raise NotImplementedError


class Cylinder(ThreeDShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def printVolume(self):
        volume = math.pi * self.radius * self.radius * self.height
        print("Volume of Cylinder =", volume)
        return volume

    def printArea(self):
        area = 2 * math.pi * self.radius * (self.radius + self.height)
        print("Area of Cylinder =", area)
        return area


class Sphere(ThreeDShape):
    def __init__(self, radius):
        self.radius = radius

    def printVolume(self):
        volume = (4 / 3) * math.pi * pow(self.radius, 3)
        print("Volume of Sphere =", volume)
        return volume

    def printArea(self):
        area = 4 * math.pi * self.radius * self.radius
        print("Area of Sphere =", area)
        return area


if __name__ == "__main__":
    cylinder = Cylinder(10, 20)
    sphere = Sphere(23.4)
    cylinder.printArea()
    cylinder.printVolume()
    sphere.printArea()
    sphere.printVolume()
