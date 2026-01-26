from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from bot.database.base import Base


from bot.groups.infra.database.models.groups import user_groups


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=True, default=False)
    referral_id = Column(Integer, nullable=True, default=False)
    giving_gift = Column(Boolean, default=False)
    subscribe_to_group = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    notifications_sent = Column(String, nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    groups = relationship(
        "Group",
        secondary=user_groups,
        back_populates="users"
    )

    def to_dict(self):
        # Непонятно зачем это нужно
        return {
            "id": self.id,
            "first_name": self.first_name,
            "username": self.username,
            "phone": self.phone,
            "referral_id": self.referral_id,
            "giving_gift": self.giving_gift,
            "subscribe_to_group": self.subscribe_to_group,
            "is_active": self.is_active,
            "notifications_sent": self.notifications_sent,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"