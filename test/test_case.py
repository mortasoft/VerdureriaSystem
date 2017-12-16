import unittest
import main


class TestCase(unittest.TestCase):
    def test_add(self):
        result = main.sum(5, 5)
        self.assertEqual(result, 10)

    def test_sign_in(self):
        result = main.ingresoAlSistema()
        self.assertEqual(result, "loggeado")


if __name__ == "__main__":
    unittest.main()
