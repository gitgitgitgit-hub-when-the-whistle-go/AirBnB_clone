#!/usr/bin/python3
"""Test cases for class Review"""

from unittest import TestCase
from models.review import Review
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCase):
    """
    Test the pycodestyle and syntax requirements
    for the `Review` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_Review(TestCase):
    """Test class Review"""

    def Test_instance(self):
        """Test instance of class Review"""
        inst_review = Review()
        self.assertTrue(issubclass(inst_review, Review))
