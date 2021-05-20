from pydantic import BaseModel, NonNegativeInt, constr


class Message(BaseModel):
    MessageID: NonNegativeInt
    Body: constr(max_length=160)
    Views: NonNegativeInt

    class Config:
        orm_mode = True

