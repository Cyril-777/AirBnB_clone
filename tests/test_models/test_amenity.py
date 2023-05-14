#!/usr/bin/env python3
'''unit test for the amenity storage class
'''
import sys
sys.path.append('../..')
import unittest
# import json # should need arise
import pep8
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenityClass(unittest.TestCase):
    '''TestAmenityClass tests for the inherited class
    Amenity. We are checking for expected outputs
    '''

    def setUp(self):
        '''set up to ensure no unnecessary repititions'''
        with open('test.json', 'w'):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""


    def tearDown(self):
        '''destroys file created for testing'''
        storage._FileStorage__file_path = 'file.json'
        try:
            os.remove('test.json')
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        '''check if module has documentation'''
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_class_doc(self):
        '''checks class for documentation'''
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_doc(self):
    	'''check for documentation in classes'''
    	for method in dir(Amenity):
    		self.assertTrue(len(method.__doc__) > 0)

    def test_pep8(self):
    	'''test that our classes conform to pep standard'''
    	pepstyle = pep8.StyleGuide(quite=True)
    	file1 = 'models/amenity.py'
    	file2 = 'tests/test_models/test_amenity.py'
    	result = pepstyle.check_files([file1, file2])
    	self.assertEqual(result.total_errors, 2, 'Found pep style errors.')

    def test_is_instance(self):
    	'''test to check if user is instance of BaseModel'''
    	new_Amenity = Amenity()
    	self.assertTrue(isinstance(new_Amenity, BaseModel))

    def test_attribute_type(self):
    	'''tests the attribute types of the user'''
    	new_Amenity = Amenity()
    	self.assertTrue(type(new_Amenity.name) == str)


if __name__ == "__main__":
    unittest.main()

