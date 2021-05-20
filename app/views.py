from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

router = APIRouter()


@router.get("/messages", response_model=List[schemas.Message])
async def get_messages(db: Session = Depends(get_db)):
    db_messages = crud.get_messages(db)
    if db_messages is None:
        raise HTTPException(status_code=404, detail="not found messageess")
    return db_messages
