# test/test_calcular.py
import unittest
from domain.motor_descuento import MotorDescuentos

class Usuario:
    """Clase simple para tests"""
    def __init__(self, codigo_vip=False, antiguedad=0):
        self.codigo_vip = codigo_vip
        self.antiguedad = antiguedad
        self.precio_base = 100.0

class MotorDescuentosTest(unittest.TestCase):

    def setUp(self):
        self.motor = MotorDescuentos()

    def test_regla_base(self):
        usuario = Usuario()
        precio = self.motor.calcular(usuario)
        self.assertEqual(precio, 100)

    def test_regla_codigo_vip(self):
        usuario = Usuario(codigo_vip=True)
        precio = self.motor.calcular(usuario)
        self.assertEqual(precio, 80)  # 20% de descuento

    def test_regla_antiguedad(self):
        usuario = Usuario(antiguedad=5)
        precio = self.motor.calcular(usuario)
        self.assertEqual(precio, 90)  # 10% de descuento

    def test_regla_limite_descuento(self):
        usuario = Usuario(codigo_vip=True, antiguedad=10)
        precio = self.motor.calcular(usuario)
        self.assertEqual(precio, 75)  # máximo 25% de descuento

if __name__ == "__main__":
    unittest.main()