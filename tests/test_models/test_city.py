#!/usr/bin/python3
"""Tests the City class"""

from models.city import City
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from unittest.mock import patch
import io


class TestCity(unittest.TestCase):
    """Test the City class"""
    the_city = City()

    def test_instance_attributes(self):
        """tests if an instance has all attributes
        that makes up a city
        """
        self.assertTrue(hasattr(TestCity.the_city, "name"))
        self.assertTrue(hasattr(TestCity.the_city, "state_id"))

    def test_default_attr_values(self):
        """tests the default set attribute values"""
        self.assertEqual(TestCity.the_city.name, "")
        self.assertEqual(TestCity.the_city.state_id, "")

    def test_city_print(self):
        """tests the format the city is printed in"""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print(TestCity.the_city)
        expected_output = (
            "[City] ({}) ".format(TestCity.the_city.id) +
            "{}".format(TestCity.the_city.__dict__)
        )


if __name__ == "__main__":
    unittest.main()
