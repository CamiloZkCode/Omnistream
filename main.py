from config import DATABASE_TYPE
from domain.services import SubscriptionService
from presentation.cli import run_cli


def seed_data_if_empty(repository):
    from domain.entities import User

    # Si no existe el usuario 1, asumimos que no hay datos
    if repository.get_by_id(1) is None:
        print("Inicializando datos (seeding)...")

        repository.save(User(1, "Carlos", 100, False))
        repository.save(User(2, "Ana", 30, False))
        repository.save(User(3, "Luis", 80, True))



# Selección de repositorio
if DATABASE_TYPE == "mysql":
    from infrastructure.database import get_mysql_connection
    from infrastructure.mysql_repository import MySQLUserRepository

    connection = get_mysql_connection()
    repository = MySQLUserRepository(connection)

elif DATABASE_TYPE == "json":
    from infrastructure.json_repository import JsonUserRepository

    repository = JsonUserRepository()

else:
    raise Exception("Tipo de base de datos no soportado.")


# Seeding (solo si está vacío)
seed_data_if_empty(repository)

# Servicio
service = SubscriptionService(repository)

# Interfaz CLI
run_cli(service)