from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models


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


def insert_new_message(db: Session, body: str):
    if 160 >= body.__len__() > 0:
        db.begin()
        db.execute("SELECT nextval('next_msg_id')")
        msg_id = db.execute("SELECT * FROM next_msg_id").fetchone()
        print(msg_id, type(msg_id))
        (a, b, c) = msg_id
        db.execute("INSERT INTO messages VALUES ({}, '{}', {})".format(a, body, 0))
        db.commit()
        return msg_id
    raise HTTPException(status_code=401, detail="Incorrect message length.")
