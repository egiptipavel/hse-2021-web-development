from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

from ..db.database import Base

SQLALCHEMY_DATABASE_URL = "postgresql://hse:password@localhost:5433/test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

db: Session = TestingSessionLocal()
