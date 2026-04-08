from domain.entities import User
from domain.repositories import UserRepository


class MySQLUserRepository(UserRepository):
    def __init__(self, connection):
        self.connection = connection

    def get_by_id(self, user_id: int):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT user_id, name, balance, has_debt, is_premium, precio_base, codigo_vip, antiguedad
            FROM users
            WHERE user_id = %s
            """,
            (user_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return User(*row)

    def save(self, user):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users
            SET is_premium = %s
            WHERE user_id = %s
        """, (user.is_premium, user.user_id))
        self.connection.commit()