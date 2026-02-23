from database.session import db
from sqlalchemy import Column, Integer, String, Boolean

class Company(db.Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True, autoincrement=True)

    service_type = Column(String)
    name = Column(String, nullable=False)
    responsible = Column(String, nullable=True)
    identity = Column(String, nullable=False)
    social_name = Column(String, nullable=False)
    profile = Column(String, nullable=False)
    status = Column(String, nullable=False)
    direct_invoicing = Column(Boolean, nullable=False)
    path_file = Column(String, nullable=True)
    reproval_message = Column(String, nullable=True)