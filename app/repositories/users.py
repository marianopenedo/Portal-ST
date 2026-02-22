from models.user import Users
from database.session import db
from sqlalchemy import select

class UserRepository():
    def __init__(self):
        self.session = db.get_session()

    def catch_all_users(self):
        return self.session.execute(select(Users)).scalars().all()