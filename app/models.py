# coding: utf-8
from sqlalchemy import CheckConstraint, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    __tablename__ = 'messages'
    __table_args__ = (
        CheckConstraint('length(("Body")::text) <= 160'),
        CheckConstraint('length(("Body")::text) > 0')
    )

    MessageID = Column(Integer, primary_key=True)
    Body = Column(String(160), nullable=False)
    Views = Column(Integer, server_default=text("0"))
