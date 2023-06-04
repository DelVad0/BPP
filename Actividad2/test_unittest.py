import unittest
from maquina_cafe import MaquinaCafe


class TestMaquinaCafe(unittest.TestCase):
    def setUp(self):
        self.maquina = MaquinaCafe()

    def test_hacer_cafe_suficiente(self):
        self.assertEqual(self.maquina.hacer_cafe(), "Café servido")

    def test_hacer_cafe_insuficiente_cafe(self):
        self.maquina.cantidad_cafe = 5
        self.assertEqual(self.maquina.hacer_cafe(), "No hay suficiente café o agua")

    def test_hacer_cafe_insuficiente_agua(self):
        self.maquina.cantidad_agua = 50
        self.assertEqual(self.maquina.hacer_cafe(), "No hay suficiente café o agua")

    def test_rellenar_cafe(self):
        self.maquina.rellenar_cafe()
        self.assertEqual(self.maquina.cantidad_cafe, 100)

    def test_rellenar_agua(self):
        self.maquina.rellenar_agua()
        self.assertEqual(self.maquina.cantidad_agua, 1000)