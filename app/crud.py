from sqlalchemy.orm import Session

from . import models


def get_messages(db: Session):
    return db.query(models.Message).all()


def get_message_by_id(db: Session, message_id: int):
    return (
        db.query(models.Message).filter(models.Message.MessageID == message_id).first()
    )


def get_messages_by_author(db: Session, author: str):
    return (
        db.query(models.Message).filter(models.Message.Author == author).all()
    )