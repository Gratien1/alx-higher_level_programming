#!/usr/bin/python3
"""
Module containing Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Validate and Initiate
        """
        super().__init__(id)
        self._update_w(width, "width")
        self._update_h(height, "height")
        self._update_x(x, "x")
        self._update_y(y, "y")

    def _validate_integer(self, value, attr_name):
        """
        Is integer
        """
        if type(value) != int:
            raise TypeError(f"{attr_name} must be an integer")

    def _validate_positive(self, value, attr_name):
        """
        Is positive (> 0)
        """
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def _validate_non_negative(self, value, attr_name):
        """
        Is no-negative (>= 0)
        """
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def _validate_integer_non_negative(self, value, attr_name):
        """Is no negative integer"""
        self._validate_integer(value, attr_name)
        self._validate_non_negative(value, attr_name)

    def _validate_integer_positive(self, value, attr_name):
        """Is positive integer"""
        self._validate_integer(value, attr_name)
        self._validate_positive(value, attr_name)

    def __str__(self):
        """
        Overriding __str__
        """
        str_1 = "{}/{} - ".format(self.__x, self.__y)
        str_2 = "{}/{}".format(self.__width, self.__height)
        return "[Rectangle] ({}) ".format(self.id) + str_1 + str_2

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self._update_w(value, "width")

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self._update_h(value, "height")

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self._update_x(value, "x")

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        self._update_y(value, "y")

    def area(self):
        """
        Return area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Display rectangle
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                for k in range(self.__x):
                    if j == 0:
                        print(" ", end='')
                print("#", end='')
            print("")

    def _update_w(self, value, attr_name):
        """update w"""
        self._validate_integer_positive(value, attr_name)
        self.__width = value

    def _update_h(self, value, attr_name):
        """update h"""
        self._validate_integer_positive(value, attr_name)
        self.__height = value

    def _update_x(self, value, attr_name):
        """update x"""
        self._validate_integer_non_negative(value, attr_name)
        self.__x = value

    def _update_y(self, value, attr_name):
        """update y"""
        self._validate_integer_non_negative(value, attr_name)
        self.__y = value

    def update(self, *args, **kwargs):
        """
        Update rectangle attrs
        """
        exist = 0
        if args:
            num = len(args)
            if num == 1:
                self.id = args[0]
            elif num == 2:
                self.id = args[0]
                self._update_w(args[1], "width")
            elif num == 3:
                self.id = args[0]
                self._update_w(args[1], "width")
                self._update_h(args[2], "height")
            elif num == 4:
                self.id = args[0]
                self._update_w(args[1], "width")
                self._update_h(args[2], "height")
                self._update_x(args[3], "x")
            elif num == 5:
                self.id = args[0]
                self._update_w(args[1], "width")
                self._update_h(args[2], "height")
                self._update_x(args[3], "x")
                self._update_y(args[4], "y")
        elif kwargs:
            keys = ["id", "width", "height", "x", "y"]
            if keys[0] in kwargs:
                self.id = kwargs[keys[0]]
            if keys[1] in kwargs:
                self._update_w(kwargs[keys[1]], keys[1])
            if keys[2] in kwargs:
                self._update_h(kwargs[keys[2]], keys[2])
            if keys[3] in kwargs:
                self._update_x(kwargs[keys[3]], keys[3])
            if keys[4] in kwargs:
                self._update_y(kwargs[keys[4]], keys[4])
