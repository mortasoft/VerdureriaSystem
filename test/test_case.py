import unittest
import main


class TestCase(unittest.TestCase):
    def test_add(self):
        result = main.sum(5, 5)
        self.assertEqual(result, 10)

    def test_sign_in(self):
        result = main.ingresoAlSistema()
        self.assertEqual(result, "loggeado")

    def test_opciones_cotizacion(self):
        result = main.seleccionarOpciones()
        self.assertEqual(result, "cotizacion")

    def test_opciones_mantenimiento(self):
        result = main.seleccionarOpciones()
        self.assertEqual(result, "mantenimiento")

    def test_opciones_informe_de_ventas_diarias(self):
        result = main.seleccionarOpciones()
        self.assertEqual(result, "informe de ventas diarias")

    def test_opciones_informe_de_ganancias_diarias(self):
        result = main.seleccionarOpciones()
        self.assertEqual(result, "informe de ganancias diarias")
    def test_opciones_salir(self):
        result = main.seleccionarOpciones()
        self.assertEqual(result, "salir")

if __name__ == "__main__":
    unittest.main()
