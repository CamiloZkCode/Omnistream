# DOMAIN/services/motor_descuentos.py

# domain/motor_descuento.py

class MotorDescuentos:

    def calcular(self, usuario):
        precio = usuario.precio_base
        descuento = 0

        # Descuento por código VIP
        if getattr(usuario, "codigo_vip", False):
            descuento += 20  # 20%

        # Descuento por antigüedad
        if getattr(usuario, "antiguedad", 0) >= 5:
            descuento += 10  # 10%

        # Limitar descuento máximo al 25%
        if descuento > 25:
            descuento = 25

        precio_final = precio * (1 - descuento / 100)
        return round(precio_final, 2)