import unittest
import app as App


class AppTestCase(unittest.TestCase):
    def test_higher_int(self):
        self.assertRaises(TypeError, App.main, "11")

    def test_lower_int(self):
        self.assertRaises(TypeError, App.main, "-5")

    def test_str_to_int(self):
        self.assertRaises(ValueError, App.main, "ten")

    def test_float_to_int(self):
        self.assertRaises(ValueError, App.main, ".5")

    def test_zero(self):
        self.assertRaises(ZeroDivisionError, App.main, "0")

    def test_correct(self):
        self.assertTrue(App.main, "5")

if __name__ == "__main__":
    unittest.main()
