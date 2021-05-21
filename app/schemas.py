from pydantic import BaseModel, NonNegativeInt, constr
from typing import Optional


class Message(BaseModel):
    MessageID: NonNegativeInt
    Body: constr(max_length=160)
    Views: NonNegativeInt

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    hashed_password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

