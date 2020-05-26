import unittest
from Test import test


class TestTest(unittest.TestCase):

    def testAdd(self):
        result = test.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
