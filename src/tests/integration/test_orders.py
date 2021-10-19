import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from ...sql_app import models
from ...sql_app.crud import create_user
from ...sql_app.database import Base
from ...sql_app.schemas import UserCreate

SQLALCHEMY_DATABASE_URL = "postgresql://hse:password@localhost:5433/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def delete_from_table(table, db: Session):
    db.query(table).delete(synchronize_session='fetch')
    db.commit()


def test_create_user(db: Session = TestingSessionLocal()):
    delete_from_table(models.User, db)
    user = UserCreate(password="password", **{"login": "login"})
    create_user(db, user)
