# motor_descuentos.py

class MotorDescuentos:
    def calcular(self, usuario):
        """
        Retorna el precio final aplicando reglas de descuento.
        Las reglas son:
        - Base: 100 si no hay descuento especial
        - Código VIP: 20% de descuento
        - Antigüedad: 10% de descuento adicional
        - Límite de descuento: máximo 25%
        """

        precio_base = 100
        descuento = 0

        # Regla código VIP
        if getattr(usuario, "codigo_vip", False):
            descuento += 20  # 20% de descuento

        # Regla antigüedad
        if getattr(usuario, "antiguedad", 0) >= 5:
            descuento += 10  # 10% adicional

        # Limitar el descuento a 25%
        if descuento > 25:
            descuento = 25

        precio_final = precio_base * (1 - descuento / 100)
        return precio_final