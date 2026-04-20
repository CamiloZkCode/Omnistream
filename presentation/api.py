# presentation/api.py
from fastapi import FastAPI, HTTPException
from config import DATABASE_TYPE
from domain.services import SubscriptionService
from domain.descuento_client import DescuentoServiceClient  # NUEVO

app = FastAPI()

# Configuración del repositorio (sin cambios)
if DATABASE_TYPE == "mysql":
    from infrastructure.database import get_mysql_connection
    from infrastructure.mysql_repository import MySQLUserRepository

    connection = get_mysql_connection()
    repository = MySQLUserRepository(connection)

else:
    from infrastructure.json_repository import JsonUserRepository
    repository = JsonUserRepository()

# NUEVO: Cliente del microservicio de descuentos
descuento_client = DescuentoServiceClient()

# Servicio con inyección del cliente
service = SubscriptionService(repository, descuento_client)


@app.post("/upgrade/{user_id}",
          responses={
        400: {
            "description": "Error de negocio"
        },
        404: {
            "description": "Usuario no encontrado"
        }
    })
def upgrade(user_id: int):
    try:
        user = service.upgrade_user(user_id)
        return {"message": "Upgrade exitoso", "user": user.__dict__}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# NUEVO ENDPOINT: Calcula el precio con descuento usando el microservicio
@app.get("/precio-con-descuento/{user_id}",
         responses={
        400: {"description": "Error al calcular el descuento"},
    })
def get_precio_con_descuento(user_id: int):
    """
    Calcula el precio final del usuario aplicando descuentos.
    Este endpoint demuestra el Strangler Fig: la lógica de descuentos
    ahora vive en el microservicio externo.
    """
    try:
        precio_final = service.calcular_precio_con_descuento(user_id)
        return {
            "user_id": user_id,
            "precio_final": precio_final,
            "message": "Descuento calculado por microservicio externo"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# NUEVO ENDPOINT: Health check del microservicio de descuentos
@app.get("/descuento-service/health")
def descuento_service_health():
    """Verifica si el microservicio de descuentos está disponible"""
    is_healthy = descuento_client.health_check()
    return {
        "status": "healthy" if is_healthy else "unhealthy",
        "service": "discount-service",
        "available": is_healthy
    }