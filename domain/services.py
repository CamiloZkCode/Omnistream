from domain.repositories import UserRepository


class SubscriptionService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def upgrade_user(self, user_id: int):
        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise Exception("Usuario no encontrado.")

        user.upgrade_to_premium()

        self.user_repository.save(user)

        return user