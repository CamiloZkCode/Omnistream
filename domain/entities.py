class User:
    def __init__(
        self,
        user_id: int,
        name: str,
        balance: float,
        has_debt: bool,
        is_premium: bool = False,
        precio_base: float = 100.0,  # este es el que estaba fallando
        codigo_vip: str = None,
        antiguedad: int = 0
    ):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.has_debt = has_debt
        self.is_premium = is_premium
        self.precio_base = precio_base
        self.codigo_vip = codigo_vip
        self.antiguedad = antiguedad

    def can_upgrade_to_premium(self) -> bool:
        return self.balance > 50 and not self.has_debt

    def upgrade_to_premium(self):
        if not self.can_upgrade_to_premium():
            raise Exception("El usuario no cumple las condiciones para ser Premium.")
        self.is_premium = True