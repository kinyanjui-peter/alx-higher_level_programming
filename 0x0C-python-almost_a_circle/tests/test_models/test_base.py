#!/usr/bin/python3
"""test case for the module base"""
import unittest
from models.base import Base
"""define class that inherit from unitest"""



class TestBaseClass(unittest.TestCase):
    """test whether an instance is successfully created"""
    def test_instance_creation_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

   
    """Test if id is negative"""
    def test_negative_id_value(self):
        obj = Base(-5)
        self.assertEqual(obj.id, -5)

    """test if id is a string"""
    def test_different_data_types_as_id(self):
        obj1 = Base("abc")
        obj2 = Base(3.14)

    """ test if id is None"""
    def test_id_set_to_none(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertNotEqual(obj1.id, obj2.id)
