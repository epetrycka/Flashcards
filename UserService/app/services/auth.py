from passlib.context import CryptContext
import jwt
import datetime
from app.config import settings
from typing import Tuple

ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN
SECRET_KEY= settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_tokens(user_id: str) -> Tuple[str, str]:
    """
    :param user_id: ID użytkownika
    :return: Krotka z Access Token i Refresh Token
    """
    now = datetime.datetime.utcnow()
    
    access_token_payload = {
        "sub": user_id,
        "exp": now + datetime.timedelta(seconds=ACCESS_TOKEN_EXPIRES_IN),
        "iat": now,
    }
    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    refresh_token_payload = {
        "sub": user_id,
        "exp": now + datetime.timedelta(seconds=REFRESH_TOKEN_EXPIRES_IN),
        "iat": now,
    }
    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return access_token, refresh_token

def verify_access_token(token: str) -> str:
    """
    :param token: Access Token
    :return: ID użytkownika (jeśli token jest ważny)
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise Exception("Access Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Access Token")
    
def refresh_access_token(refresh_token: str) -> str:
    """
    :param refresh_token: Refresh Token
    :return: Nowy Access Token
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["sub"]
        access_token, _ = generate_tokens(user_id)
        return access_token
    except jwt.ExpiredSignatureError:
        raise Exception("Refresh Token has expired, user must log in again")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Refresh Token")