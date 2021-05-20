from sqlalchemy import (
    Column,
    Date,
    Integer,
    String,
)
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import NullType

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = "messages"

    MessageID = Column(Integer, primary_key=True)
    Body = Column(String(160), nullable=False)
    Author = Column(String(40), nullable=False)
    Views = Column(Integer)
    PublishDate = Column(Date)


# class User(Base):
#     __tablename__ = "users"

