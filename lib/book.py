#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count, year):
        self.title = title
        self._page_count = page_count
        self.year = year

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            raise ValueError("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"
