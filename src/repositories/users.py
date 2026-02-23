from schemas.user_info import UserSchema
from models.user import Users
from database.session import db
from sqlalchemy import or_, select, update, delete

class UserRepository():
    def __init__(self):
        self.session = db.get_session()

    def catch_all_users(self):
        return self.session.execute(select(Users)).scalars().all()

    def update_user(self, user_id: int, user: UserSchema) -> None:
        self.session.execute(
            update(Users)
            .where(Users.id == user_id)
            .values(**user.model_dump(exclude_unset=True))
        )

        self.session.commit()

    def get_by_login(self, login: str) -> Users:
        user = self.session.execute(
            select(Users)
            .where(
                or_(
                    Users.login == login,
                    Users.cnpj == login,
                    Users.cpf == login
                ))).scalars().first()

        return user        

    def create_new_user(self, user: UserSchema) -> Users:
        new_user = Users(**user.model_dump())
        self.session.add(new_user)
        self.session.commit()

    def delete_user(self, user_id: int):
        self.session.execute(delete(Users).where(Users.id == user_id))