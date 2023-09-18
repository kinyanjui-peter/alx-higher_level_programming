#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance"""
        super().__init__(id) #calling superclass
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    """that returns the area value of the Rectangle instance."""
    def area(self):
        return self.__width * self.__width

    """ prints in stdout the Rectangle instance with the character #"""
    def display(self):
        for _ in range(self.__y):
            print('$')
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width + '$')

    """overriding the __str__ method with my output format"""
    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.x} - {self.width}/{self.height}")

    """add the public method that assigns an argument to each attribute:"""
    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                self.id = args[0]
            if len(args) > 2:
                self.width = args[1]
            if len(args) > 3:
                self.height = args[2]
            if len(args) > 4:
                self.x = args[3]
            if len(args) > 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
