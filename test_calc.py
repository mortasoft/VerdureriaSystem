import unittest
import main


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = main.sum(5, 5)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
