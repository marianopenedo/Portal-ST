from database.session import db
from sqlalchemy import Column, Integer, String, Boolean

class Users(db.Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)

    login = Column(String)
    cpf = Column(String, nullable=True)
    cnpj = Column(String, nullable=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)
    user_type = Column(String, nullable=False)