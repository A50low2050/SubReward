from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    first_name: str
    username: str
    phone: str = False
    referral_id: int = False
    giving_gift: bool = False
    subscribe_to_group: bool = False
    is_active: bool = True
    notifications_sent: str = True
    group_name: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    @classmethod
    def create(
            cls,
            id,
            first_name,
            username,
            group_name=None,

    ) -> 'User':

        return cls(
            id=id,
            first_name=first_name,
            username=username,
            group_name=group_name,
        )


    def deactivate(self) -> None:
        self.is_active = False
        self.updated_at = datetime.now()