from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models
from .login import validate_token


def get_messages(db: Session):
    return db.query(models.Message).all()


def get_message_by_id(db: Session, message_id: int):
    return (
        db.query(models.Message).filter(models.Message.MessageID == message_id).first()
    )


def get_user_by_username(db: Session, username: str):
    return (
        db.query(models.User).filter(models.User.Username == username).first()
    )


def insert_new_message(db: Session, token: str, body: str):
    if 160 >= body.__len__() > 0:
        if validate_token(db, token):
            db.begin()
            msg_id = db.execute("SELECT nextval('next_msg_id')")
            db.execute("INSERT INTO messages VALUES (?)", (msg_id, body,))
            db.commit()
            return msg_id
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")
    raise HTTPException(status_code=401, detail="Incorrect message length.")
