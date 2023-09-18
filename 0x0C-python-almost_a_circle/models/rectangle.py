#!/usr/bin/python3

"""Child class Rectangle that inherits from the Base class"""

from models.base import Base


class Rectangle(Base):
    """
    A subclass of the Base class representing rectangles.
    The Rectangle class inherits from the Base class and defines
    private instance attributes, each with its own public getter and setter:
    - width (corresponds to __width)
    - height (corresponds to __height)
    - x (corresponds to __x)
    - y (corresponds to __y)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances of the Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Call the constructor of the superclass

    @property
    def width(self):
        """Retrieve the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set and validate the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set and validate the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set and validate the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set and validate the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the Rectangle using '#' characters"""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes of the Rectangle"""

        attribute_order = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attribute_order[i], args[i])

        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle"""
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
