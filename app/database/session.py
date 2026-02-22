from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


class Database:
    def __init__(self):
        self.DATABASE_URL = (
            "mssql+pyodbc://sa:Admin%401234@db:1433/master?"
            "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
        )

        self.engine = create_engine(
            self.DATABASE_URL,
            echo=True,
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
