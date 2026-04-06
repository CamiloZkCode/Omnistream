from fastapi import FastAPI, HTTPException
from config import DATABASE_TYPE
from domain.services import SubscriptionService

app = FastAPI()

if DATABASE_TYPE == "mysql":
    from infrastructure.database import get_mysql_connection
    from infrastructure.mysql_repository import MySQLUserRepository

    connection = get_mysql_connection()
    repository = MySQLUserRepository(connection)

else:
    from infrastructure.json_repository import JsonUserRepository
    repository = JsonUserRepository()

service = SubscriptionService(repository)


@app.post("/upgrade/{user_id}")
def upgrade(user_id: int):
    try:
        user = service.upgrade_user(user_id)
        return {"message": "Upgrade exitoso", "user": user.__dict__}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))