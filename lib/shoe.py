#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self._size = size
        self.color = color
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise ValueError("size must be an integer")
        self._size = value

    def cobble(self):
        self.condition = "Repaired"
        return "Your shoe is as good as new!"
