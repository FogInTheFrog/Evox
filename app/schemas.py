from pydantic import BaseModel, NonNegativeInt, constr
from typing import Optional
from datetime import datetime


class Message(BaseModel):
    MessageID: NonNegativeInt
    Body: constr(min_length=1, max_length=160)
    Author: constr(max_length=40)
    Views: NonNegativeInt
    PublishDate: datetime

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     email: str
#
#
# class UserCreate(UserBase):
#     password: str
#
#
# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []
#
#     class Config:
#         orm_mode = True