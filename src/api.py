from dataclasses import dataclass
from typing import Final

ID: Final[int] = 1
NAME: Final[str] = "Adi"


@dataclass
class User:
    id: int
    name: str

    @staticmethod
    def can_fly() -> bool:
        return False

    @staticmethod
    def refresh() -> None:
        print("Refreshing data...")

    def status(self) -> str:
        return f"{self.name} is a user"


def get_user() -> User:
    return User(id=ID, name=NAME)
