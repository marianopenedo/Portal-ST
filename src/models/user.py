from database.session import db
from sqlalchemy import Column, Integer, String

class Users(db.Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    login = Column(String(200), unique=True, primary_key=True)
    cpf = Column(String(11), nullable=True)
    cnpj = Column(String(14), nullable=True)
    email = Column(String(200), nullable=True)
    password = Column(String, nullable=False)
    user_type = Column(String, nullable=False)