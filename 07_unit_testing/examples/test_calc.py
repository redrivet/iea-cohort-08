import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        expected = 3
        result = calc.add(1, 2)
        self.assertEqual(result, expected)

    def test_add_negative(self):
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(-1, -2), -3)

    def test_add_string(self):
        expected = '12'
        result = calc.add('1', '2')
        self.assertEqual(result, expected)

    def test_add_string_to_int(self):
        with self.assertRaises(TypeError):
            calc.add(1, '2') 

    def test_add_float_to_int(self):
        expected = 3.0
        result = calc.add(2.0, 1)
        self.assertEqual(expected, result)
