# domain/services.py
from domain.repositories import UserRepository
from domain.descuento_client import DescuentoServiceClient  # NUEVO


class SubscriptionService:

    def __init__(self, user_repository: UserRepository, descuento_client: DescuentoServiceClient = None):
        self.user_repository = user_repository
        # Si no se provee cliente, se crea uno por defecto
        self.descuento_client = descuento_client or DescuentoServiceClient()

    def upgrade_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise ValueError("Usuario no encontrado.")

        user.upgrade_to_premium()

        self.user_repository.save(user)

        return user
    
    def calcular_precio_con_descuento(self, user_id: int) -> float:
        """
        NUEVO MÉTODO: Calcula el precio final del usuario aplicando descuentos
        usando el microservicio (Strangler Fig)
        """
        user = self.user_repository.get_by_id(user_id)
        
        if user is None:
            raise ValueError("Usuario no encontrado en la base de datos.")
        
        # AQUÍ OCURRE EL STRANGLER FIG
        # En lugar de llamar a MotorDescuentos.calcular() localmente,
        # llamamos al microservicio externo
        return self.descuento_client.calcular(
            precio_base=user.precio_base,
            codigo_vip=user.codigo_vip,
            antiguedad=user.antiguedad
        )