import unittest

from quantity_1 import Quantity

quantity = Quantity()


class QuantityMeasurement(unittest.TestCase):

    def test_get_quantity(self):
        expected = quantity.get_number_of_quantity(3)
        self.assertEqual(3, expected)

    def test_quantity_measurement_valid_case(self):
        expected = quantity.get_number_of_quantity(4)
        expected = quantity.quantity_measurement(5, 6)
        self.assertEqual(True, expected)

    def test_quantity_measurement_invalid_case(self):
        expected = quantity.get_number_of_quantity(4)
        expected = quantity.quantity_measurement(5, 5)
        self.assertNotEqual(False, expected)


if __name__ == '__main__':
    unittest.main()
