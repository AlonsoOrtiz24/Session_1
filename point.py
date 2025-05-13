import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object
        :param x: the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x #Define x attribute via self.x
        self.y = y #and assign the value x to it

    def __str__(self):
        """
        Magic method that is called when we try to print an instance
        :return: <x, y>
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):
        """
        Returns the official string representation of the point,
        using the same format as __str__.
        """
        return self.__str__()  # use the same way of printing as str

    def distance_orig(self):
        """
        Calculates the distance from the origin (0,0) to this point.

        Returns:
            float: The Euclidean distance.
        """
        return (self.x**2 + self.y**2)**0.5  # Square root of the sum of x and y squared

    def __gt__(self, other):
        """
        Compares if this point is farther from the origin than another point.

        Returns:
            bool: True if this point's distance is greater than the other's.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Checks if this point has the same distance from the origin as another point.

        Returns:
            bool: True if both points are equally distant from the origin.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance
