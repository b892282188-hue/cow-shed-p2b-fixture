import unittest

from mathutils import add, clamp, subtract


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)


class TestClamp(unittest.TestCase):
    def test_value_inside_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_value_below_low(self):
        self.assertEqual(clamp(-1, 0, 10), 0)

    def test_value_above_high(self):
        self.assertEqual(clamp(11, 0, 10), 10)

    def test_value_at_low(self):
        self.assertEqual(clamp(0, 0, 10), 0)

    def test_value_at_high(self):
        self.assertEqual(clamp(10, 0, 10), 10)

    def test_low_above_high(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)


if __name__ == "__main__":
    unittest.main()
