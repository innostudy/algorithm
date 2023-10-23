import unittest
from garam import solution


class TestStringMethods(unittest.TestCase):

    def test0(self):
        self.assertEqual(solution([149, 180, 192, 170], 167), 3)

    def test1(self):
        self.assertEqual(solution([180, 120, 140], 190), 0)


if __name__ == '__main__':
    unittest.main()
