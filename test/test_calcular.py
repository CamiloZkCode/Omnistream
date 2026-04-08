import unittest
from datetime import datetime, timedelta
from domain.entities import User

# La clase MotorDescuentos aún no tiene lógica
from domain.motor_descuento import MotorDescuentos

class MotorDescuentosTest(unittest.TestCase):

    def setUp(self):
        # Usuario premium con fecha de registro simulada
        self.user = User(1, "Carlos", 100, False, is_premium=True)
        self.user.registration_date = datetime.now() - timedelta(days=400)  # >1 año

    def test_regla_base(self):
        motor = MotorDescuentos()
        precio = motor.calcular_precio_final(self.user, codigo=None)
        self.assertEqual(precio, 100)  # Debe fallar

    def test_regla_antiguedad(self):
        motor = MotorDescuentos()
        precio = motor.calcular_precio_final(self.user, codigo=None)
        self.assertEqual(precio, 90)  # Debe fallar

    def test_regla_codigo_vip(self):
        motor = MotorDescuentos()
        precio = motor.calcular_precio_final(self.user, codigo="OMNI20")
        self.assertEqual(precio, 80)  # Debe fallar

    def test_regla_limite_descuento(self):
        motor = MotorDescuentos()
        precio = motor.calcular_precio_final(self.user, codigo="OMNI20")
        self.assertEqual(precio, 75)  # Debe fallar

if __name__ == "__main__":
    unittest.main()