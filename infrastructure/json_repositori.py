import json
import os
from domain.entities import User
from domain.repositories import UserRepository
from config import JSON_FILE


class JsonUserRepository(UserRepository):

    def __init__(self):
        if not os.path.exists(JSON_FILE):
            with open(JSON_FILE, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(JSON_FILE, "r") as f:
            return json.load(f)

    def _save_all(self, data):
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def get_by_id(self, user_id: int):
        users = self._load()
        for u in users:
            if u["user_id"] == user_id:
                return User(**u)
        return None

    def save(self, user):
        users = self._load()

        for i, u in enumerate(users):
            if u["user_id"] == user.user_id:
                users[i] = user.__dict__
                self._save_all(users)
                return

        users.append(user.__dict__)
        self._save_all(users)