from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from bot.database.base import Base

# Association Table for User and Group
user_groups = Table(
    'user_groups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    users = relationship(
        "Users",
        secondary=user_groups,
        back_populates="groups"
    )

    def __repr__(self):
        return f"<Group(id={self.id}, name='{self.name}')>"
