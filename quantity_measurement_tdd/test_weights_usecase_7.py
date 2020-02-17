from weights_4 import CompareWeights
import unittest

weight = CompareWeights()


class TestWeights(unittest.TestCase):

    def test_kg_eq_grams(self):
        expected = weight.convert_kg_into_grams(2)
        self.assertEqual(2000, expected)

    def test_grams_into_kgs(self):
        expected = weight.convert_grams_into_kg(2500)
        self.assertEqual(2.5, expected)

    def test_kg_neq_grams(self):
        expected = weight.convert_kg_into_grams(3)
        self.assertNotEqual(2500, expected)

    def test_add_tonne_and_gram_get_kgs(self):
        expected = weight.add_tonne_into_grams_get_kg(1, 1000)
        self.assertEqual(1001.0, expected)

    def test_tonne_eq_kgs(self):
        expected = weight.convert_tonne_into_kg(2)
        self.assertEqual(2000, expected)


if __name__ == '__main__':
    unittest.main()
