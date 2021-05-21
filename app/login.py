from fastapi import Depends,  HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional

from .crud import get_user_by_username
from .database import get_db
from .schemas import User, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "353c29ef6bd0b52c4c3b1b146254112e972fe588096d0c7cdbd18881df816795"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


def validate_token(token: str):
    token_exception = HTTPException(
        status_code=403,
        detail="Invalid token or expired token.",
        headers={"WWW-Authenticate": "Bearer"}
    )
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise token_exception
    except JWTError:
        raise credentials_exception
    return True


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    if validate_token(token):
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_data = TokenData(username=username)
        user = get_user_by_username(db, token_data.username)
        if user is None:
            raise HTTPException(status_code=401, detail="Unsuccessful authorisation")
        return user
    else:
        raise HTTPException(status_code=401, detail="can't get current user")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    print(user.__dict__)
    print(user.Username, user.Hashed_password, user.Fullname)
    user_db = User.from_orm(user)
    if not user:
        return False
    print(user_db.Username, user_db.Hashed_password, user_db.Fullname)
    if not verify_password(password, user_db.Hashed_password):
        return False
    return user_db


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
