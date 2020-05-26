import unittest
from N001N010.N001Multiply import multiply


class TestTest(unittest.TestCase):

    def test_add_1(self):
        result = multiply.multiply(2, 4)
        self.assertEqual(result, 8)

    def test_add_2(self):
        result = multiply.multiply(1, 4)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
