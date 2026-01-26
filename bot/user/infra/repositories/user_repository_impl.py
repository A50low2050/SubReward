from sqlalchemy.orm import Session
from bot.groups.infra.database.models.groups import Group
from bot.user.domain.entities.user import User
from bot.user.domain.repositories.user_repository import IUserRepository
from bot.user.infra.database.models.users import Users


class UserRepository(IUserRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        user_model = self.session.query(Users).filter_by(id=user.id).first()

        if user_model:
            user_model.first_name = user.first_name
            user_model.username = user.username
            user_model.is_active = user.is_active
            if user.group_name:
                user_model.groups.clear()
                self._create_user_group(user_model, user.group_name)
        else:
            user_model = Users(
                id=user.id,
                first_name=user.first_name,
                username=user.username,
                is_active=user.is_active,
            )
            self.session.add(user_model)
            if user.group_name:
                self._create_user_group(user_model, user.group_name)
        self.session.commit()
        return user

    def _create_user_group(self, user: Users, group_name: str):
        group = self.session.query(Group).filter_by(name=group_name).first()
        if not group:
            group = Group(name=group_name)
            self.session.add(group)
            self.session.flush()

        user.groups.append(group)

    def delete(self, user_id: int) -> bool:
        user_model = self.session.query(Users).filter_by(id=user_id).first()
        if user_model:
            self.session.delete(user_model)
            self.session.commit()
            return True
        return False
