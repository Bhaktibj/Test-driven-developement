from volumes_3 import CompareVolumes
import unittest

volume = CompareVolumes()


class TestVolumes(unittest.TestCase):

    def test_gallons_eq_liter(self):
        expected = volume.convert_gallons_liter(1)
        self.assertEqual(3.78, expected)

    def test_liter_eq_ml(self):
        expected = volume.convert_liters_to_ml(1)
        self.assertEqual(1000, expected)

    def test_add_of_gallon_and_liter_get_liter(self):
        expected = volume.additions_of_gallon_and_ltr(1, 3.78)
        self.assertEqual(7.56, expected)

    def test_add_liter_in_ml_get_liter(self):
        expected = volume.additions_of_liter_and_ml(1, 1000)
        self.assertEqual(2, expected)


if __name__ == '__main__':
    unittest.main()
