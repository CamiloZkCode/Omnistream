from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int):
        pass

    @abstractmethod
    def save(self, user):
        pass