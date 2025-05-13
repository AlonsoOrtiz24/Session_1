from point import Point
import random

class PointException(Exception):
    """
    Custom exception for errors related to point operations or attributes.
    """
    pass

class ColorPoint(Point):
    """
    Represents a 2D point with an associated color.
    Inherits coordinates and methods from the Point class, and adds a color attribute.
    """

    def __init__(self, x, y, color):
        """
        Initializes a ColorPoint with coordinates (x, y) and a color.

        Uses:
            x (int or float): The x-coordinate of the point.
            y (int or float): The y-coordinate of the point.
            color (str): The color associated with the point.

        Raises:
            PointException: If x or y is not a numeric value.
        """
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int,float)):
            raise PointException("y must be a number")

        super().__init__(x, y)  # Delegates initialization of x and y to Point
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the ColorPoint.

        Returns:
            str: A string in the format "<color: x, y>".
        """
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1,2,"red")
print(p.distance_orig())  # Assumes distance_orig() is defined in Point
print(p)

#colors = ["red", "green", "blue", "yellow", "black", "magenta",
#          "cyan", "white", "burgundy", "periwinkle", "marsala"]
#color_points = []
#for i in range(10):
#    color_points.append(
#        ColorPoint(random.randint(-10,10),
#                   random.randint(-10, 10),
#                   random.choice(colors)))

#print(color_points)
#color_points.sort()
#print(color_points)