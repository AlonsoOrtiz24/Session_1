from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    Represents a point in 2D space with an associated color.
    Inherits from ColorPoint and extends functionality with color validation,
    class methods, static methods, and distance calculations.
    """
    COLORS = ["red", "blue", "yellow", "green", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initializes an AdvancedPoint with coordinates (x, y) and a valid color.

        Raises:
            PointException: If the color is not in the allowed COLORS list.
        """
        if color not in self.COLORS:
            raise PointException(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Gets the x-coordinate of the point.

        Returns:
            float: x-coordinate.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Sets the x-coordinate of the point.

        """
        self._x = value

    @property
    def y(self):
        """
        Gets the y-coordinate of the point.

        Returns:
            float: y-coordinate.
        """
        return self._y

    @property
    def color(self):
        """
        Gets the color of the point.

        Returns:
            str: The color name.
        """
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Adds a new valid color to the class-level COLORS list.


        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Creates a new AdvancedPoint from a tuple of (x, y) and optional color.


        Returns:
            AdvancedPoint: A new point instance.
        """
        x, y = coordinate
        return AdvancedPoint(x,y,color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Computes Euclidean distance between two AdvancedPoint instances.

        Returns:
            float: Distance between p1 and p2.
        """
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    def distance_to_other(self,p):
        """
        Computes Euclidean distance from this point to another.

        Returns:
            float: Distance between self and p.
        """
        return ((self.x - p.x)**2 + (self.y - p.y)**2)**0.5


# Example usage
AdvancedPoint.add_color("rojo")
p = AdvancedPoint(1,2, "rojo")
print(p.x)
print(p)
print(p.distance_orig())  # Assuming distance_orig() is inherited from ColorPoint
p2 = AdvancedPoint.from_tuple((3,2))
print(p2)
print(AdvancedPoint.distance_2_points(p,p2))
print(p.distance_to_other(p2))