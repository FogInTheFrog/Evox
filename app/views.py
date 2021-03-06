from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from . import schemas, crud
from .database import get_db
from .login import get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, oauth2_scheme, \
    validate_token
from .schemas import User

router = APIRouter()


@router.get("/messages", response_model=List[schemas.Message])
async def get_messages(db: Session = Depends(get_db)):
    db_messages = crud.get_messages(db)
    if db_messages is None:
        raise HTTPException(status_code=404, detail="messages not found")
    return db_messages


@router.get("/users/me", response_model=dict)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return {"username:": current_user.Username, "full name": current_user.Fullname}


@router.post("/token")
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.Username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/messages/{msg_id}", response_model=schemas.Message)
async def get_messages(msg_id: int, db: Session = Depends(get_db)):
    db_messages = crud.get_message_by_id(db, msg_id)
    if db_messages is None:
        raise HTTPException(status_code=404, detail="message not found")
    return db_messages


@router.post("/messages/create", status_code=201)
async def create_message(message_body: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    if validate_token(token):
        new_msg_id = crud.insert_new_message(db, message_body)
        return {"New Message Created with ID:": new_msg_id, "content": message_body}
    else:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")


@router.patch("/messages/edit/{msg_id}", response_model=schemas.Message)
async def update_message_body(msg_id: int, message_body: str, db: Session = Depends(get_db),
                              token: str = Depends(oauth2_scheme)):
    if validate_token(token):
        return crud.edit_message(db, message_body, msg_id)
    else:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")


@router.delete("/messages/delete/{msg_id}", status_code=202)
async def delete_message(msg_id: int,  db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    if validate_token(token):
        crud.delete_message(db, msg_id)
        return {"Message Successfully Deleted"}
    else:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")
