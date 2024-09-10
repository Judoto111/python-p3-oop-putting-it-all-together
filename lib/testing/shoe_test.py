#!/usr/bin/env python3

from shoe import Shoe
import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        shoe = Shoe("Adidas", 9, "Red")
        assert shoe.brand == "Adidas"
        assert shoe.size == 9
        assert shoe.color == "Red"

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        shoe = Shoe("Adidas", 9, "Red")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            shoe.size = "not an integer"
        except ValueError:
            assert captured_out.getvalue().strip() == "size must be an integer"
        finally:
            sys.stdout = sys.__stdout__

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        shoe = Shoe("Adidas", 9, "Red")
        result = shoe.cobble()
        assert result == "Your shoe is as good as new!"
        assert shoe.condition == "Repaired"

    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        shoe = Shoe("Adidas", 9, "Red")
        shoe.cobble()
        assert shoe.condition == "Repaired"

   
