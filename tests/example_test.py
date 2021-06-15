import unittest
from unittest import TestCase

from src.example_folder_1.example_folder_2 import example

class TestMethods(TestCase):
    def test_example(self):
        self.assertEqual(method_1, "I am the method 1!")
if __name__ == "__main__":
     unittest.main()
