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

    def test_mantenimiento_ingreso_de_productos(self):
        result = main.ingresoDeProductos("Maíz")
        esperado = {'nombre': 'Maíz', 'kilos': 2, 'precio_de_compra': 200, 'precio_de_venta': 210, 'fecha_vencimiento': '12'}
        self.assertEqual(result, esperado)


if __name__ == "__main__":
    unittest.main()
