import unittest
from domain.entities import User
from domain.services import SubscriptionService


class FakeRepository:
    def __init__(self, user):
        self.user = user

    def get_by_id(self, user_id):
        return self.user

    def save(self, user):
        self.user = user


class TestSubscription(unittest.TestCase):

    def test_upgrade_success(self):
        user = User(1, "Test", 100, False)
        repo = FakeRepository(user)
        service = SubscriptionService(repo)

        result = service.upgrade_user(1)

        self.assertTrue(result.is_premium)

    def test_upgrade_fail_balance(self):
        user = User(1, "Test", 30, False)
        repo = FakeRepository(user)
        service = SubscriptionService(repo)

        with self.assertRaises(Exception):
            service.upgrade_user(1)


if __name__ == "__main__":
    unittest.main()