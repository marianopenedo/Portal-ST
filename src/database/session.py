from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from settings import settings


class Database:
    def __init__(self):
        self.DATABASE_URL = (
            settings.URL_DATABASE
        )

        self.engine = create_engine(
            self.DATABASE_URL,
            pool_pre_ping=True
        )

        self.session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

        self.Base = declarative_base()

    def get_session(self):
        return self.session()

    def create_tables(self):
        self.Base.metadata.create_all(bind=self.engine)

db = Database()
