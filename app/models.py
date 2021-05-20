from sqlalchemy import (
    Column,
    Date,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"
    MessageID = Column(Integer, primary_key=True)
    # MessageID = Column(Integer, primary_key=True, index=True)
    # Title = Column(String(30))
    Body = Column(String(160))
    Author = Column(String(40))
    Views = Column(Integer, default=0)
    PublishDate = Column(Date, default=datetime.now)


# class User(Base):
#     __tablename__ = "users"

