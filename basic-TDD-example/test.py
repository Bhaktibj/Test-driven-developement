from airthmatic_operations import AirthmaticOperations
import unittest


class AirthmaticOperationsTests(unittest.TestCase):

    def setUp(self):
        self.cal = AirthmaticOperations()

    def test_addition_method(self):
        result=self.cal.addition(4, 2)
        self.assertEqual(6, result)

    def test_addition_method_invalid_value(self):
        self.assertRaises(ValueError, self.cal.addition, "five", "three")

    def test_substraction_method(self):
        result=self.cal.substraction(6, 4)
        self.assertEqual(2, result)

    def test_substraction_method_invalid_output(self):
        result=self.cal.substraction(6, 4)
        self.assertNotEqual(3, result)

    def test_substraction_method_invalid_value(self):
        self.assertRaises(ValueError, self.cal.substraction, "four", "five")

    def test_multiplication_method(self):
        result=self.cal.multiplication(10, 3)
        self.assertEqual(30, result)

    def test_multiplication_method_invalid_value(self):
        self.assertRaises(ValueError, self.cal.multiplication, "four", "five")

    def test_div_method(self):
        result=self.cal.division(5, 1)
        self.assertEqual(5, result)

    def test_div_method_invalid_value(self):
        self.assertRaises(ValueError, self.cal.division, "five", "four")

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, self.cal.division, 5, 0)


if __name__ == '__main__':
    unittest.main()
