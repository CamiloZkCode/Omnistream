from domain.entities import User
from domain.repositories import UserRepository
from decimal import Decimal  # NUEVO


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
        
        # Convertir Decimal a float
        balance = float(row[2]) if isinstance(row[2], Decimal) else row[2]
        precio_base = float(row[5]) if isinstance(row[5], Decimal) else row[5]
        
        return User(
            user_id=row[0],
            name=row[1],
            balance=balance,
            has_debt=bool(row[3]),
            is_premium=bool(row[4]),
            precio_base=precio_base,
            codigo_vip=row[6],
            antiguedad=row[7]
        )

    def save(self, user):
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE users
            SET is_premium = %s
            WHERE user_id = %s
        """, (user.is_premium, user.user_id))
        self.connection.commit()