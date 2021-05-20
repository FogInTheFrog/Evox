from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://ydngzomzuxbljj:780eab665c7186ffb7c37b6ef0de6266a165f9cec5078e847a7d0eb7c748df2e@ec2-54-220-35-19.eu-west-1.compute.amazonaws.com/dfi06co5hcsmuh"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
