#!/usr/bin/python3
'''unit test for base class model
'''
import sys
sys.path.append('../..')
import unittest
# import json # should need arise
import pep8
from models import base_model
from models.amenity import Amenity
from models.base_model import BaseModel
#from engine import file_storage
from models import storage
import os
from datetime import datetime


class TestBaseClass(unittest.TestCase):
    '''Testing the BaseClass to which all others inherit
    '''

    maxDiff = None

    def setUp(self):
    	'''set up to ensure no unnecessary repititions'''

    	with open('test.json', 'w'):
    	    FileStorage._FileStorage__file_path = "test.json"
    	    FileStorage._FileStorage__objects = {}

    def tearDown(self):
    	'''destroys file created for testing'''
    	FileStorage._FileStorage__file_path = 'file.json'
    	try:
    	    os.remove('test.json')
    	except FileNotFoundError:
    	    pass

    def test_module_doc(self):
    	'''check if the module has documentation'''
    	self.assertTrue(len(Base_Model.__doc__) > 0)


    def test_class_doc(self):
    	'''checks class for documentation'''
    	self.assertTrue(len(Base_Model.__doc__) > 0)

    def test_method_doc(self):
    	'''check for documentation in classes'''
    	for method in dir(BaseModel):
    	    self.assertTrue(len(method.__doc__) > 0)

    def test_pep8(self):
    	'''test that our classes conform to pep standard'''
    	pepstyle = pep8.StyleGuide(quite=True)
    	file1 = 'models/base_model.py'
    	file2 = 'tests/test_models/test_base_model.py'
    	result = pepstyle.check_files([file1, file2])
    	self.assertEqual(result.total_errors, 2, 'Found pep style errors.')


    def test_datetime_type(self):
    	'''test the datetime type'''
    	new = BaseModel()
    	self.assertTrue(type(new.created_at) == datetime)


    def test_id_type(self):
    	'''test the id type'''
    	new = BaseModel()
    	self.assertTrue(type(new.id) == str)

    def test_str(self):
    	'''testing the string output of the class'''
    	new = BaseModel()
    	self.assertEqual(new.__str__(), "[" + new.__class__.__name__ + "]" " (" + new.id + ") " + str(new.__dict__))

    def test_id_creation(self):
    	'''check that the ids are unique to each instance'''
    	id1 = BaseModel()
    	id2 = BaseModel()
    	self.assertTrue(id1 != id2)

    def test_to_dict(self):
    	'''test the dict function'''
    	new = BaseModel()
    	my_model = new.to_dict()
    	self.assertTrue(type(my_model['created_at'] == str))
    	self.assertTrue(type(my_model['updated_at'] == str))
    	self.assertTrue(type(new.created_at) == datetime)
    	self.assertTrue(type(new.updated_at) == datetime)
    	self.assertEqual(my_model['created_at'], new.created_at.isoformat())
    	self.assertEqual(my_model['updated_at'], new.updated_at.isoformat())

    def test_is_instance(self):
    	'''checking if object is an instance of the class'''
    	obj = BaseModel()
    	self.assertEqual(BaseModel, obj)

    def test_save(self):
    	'''testing ifsave method works accordingly'''
    	new = BaseModel()
    	prev = new.updated_at
    	new.save()
    	original = new.updated_at
    	self.assertTrue(original > prev)


if __name__ == "__main__":
    unittest.main()
