import unittest
from N001N010.N001Multiply import multiply


class TestTest(unittest.TestCase):

    def testAdd(self):
        result = multiply.multiply(2, 4)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
