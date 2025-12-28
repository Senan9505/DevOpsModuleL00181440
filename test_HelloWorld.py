import unittest
from HelloWorld import get_message, check_condition

class TestHelloWorld(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello World")

    def test_check_condition_yes(self):
        #Condition is 1+6<6, which is False, should return "No"
        self.assertEqual(check_condition(), "No")

if __name__ == "__main__":
    unittest.main()

