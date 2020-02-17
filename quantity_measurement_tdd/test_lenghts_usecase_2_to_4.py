from lenghts_2 import ComapareLengths
import unittest

len = ComapareLengths()


class TestCompareLengths(unittest.TestCase):

    def test_feet_eq_yards(self):
        expected = len.convert_feet_into_yards(3)
        self.assertEqual(1, expected)

    def test_feet_neq_yards(self):
        expected = len.convert_feet_into_yards(1)
        self.assertNotEqual(1, expected)

    def test_inch_neq_yards(self):
        expected = len.convert_inch_into_yards(1)
        self.assertNotEqual(1, expected)

    def test_yards_eq_inch(self):
        expected = len.convert_yards_into_inch(1)
        self.assertEqual(36, expected)

    def test_inch_eq_yards(self):
        expected = len.convert_inch_into_yards(36)
        self.assertEqual(1, expected)

    def test_yards_eq_feet(self):
        expected = len.convert_yards_into_feet(1)
        self.assertEqual(3, expected)

    def test_inch_eq_cm(self):
        expected = len.convert_inch_into_cm(2)
        self.assertEqual(5.08001016002032, expected)

    def test_addition_of_inch(self):
        expected = len.add_inches(2, 2)
        self.assertEqual(4, expected)

    def test_addition_of_feet_and_inch(self):
        expected = len.add_feet_and_inch(1, 2)
        self.assertEqual(14, expected)

    def test_additions_of_feet_eq_inch(self):
        expected = len.add_feet_and_get_inch(1, 1)
        self.assertEqual(24, expected)

    def test_addition_of_inch_cm(self):
        expected = len.add_inch_and_cm_get_inch(2.0, 2.5)
        self.assertEqual(2.98425, expected)


if __name__ == '__main__':
    unittest.main()
