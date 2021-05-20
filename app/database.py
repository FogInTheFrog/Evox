from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://joelitpxahiqgt:ffe6958df7eb1e9f250d1e557ad63e829c4114c7c90bad2ad2adefffc8800cc4@ec2-52-213-119-221.eu-west-1.compute.amazonaws.com/dfmu8mbnjpm39u"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
