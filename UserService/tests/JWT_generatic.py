import jwt
import datetime
from typing import Tuple

ALGORITHM = "HS256"
SECRET_KEY = "ycrdzA8n0p0MA1h3+mJz8HKxHA94QK7lbXIEXZuu4mQ="
ACCESS_TOKEN_EXPIRES_IN = 3600
REFRESH_TOKEN_EXPIRES_IN = 86400

def generate_tokens(user_id: str) -> Tuple[str, str]:
    """
    :param user_id: ID użytkownika
    :return: Krotka z Access Token i Refresh Token
    """
    now = datetime.datetime.utcnow()
    
    print(now + datetime.timedelta(seconds=ACCESS_TOKEN_EXPIRES_IN))

    access_token_payload = {
        "sub": user_id,
        "exp": now + datetime.timedelta(seconds=ACCESS_TOKEN_EXPIRES_IN),
        "iat": now,
    }

    print(access_token_payload)

    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    print(access_token)

    refresh_token_payload = {
        "sub": user_id,
        "exp": now + datetime.timedelta(seconds=REFRESH_TOKEN_EXPIRES_IN),
        "iat": now,
    }

    print(refresh_token_payload)

    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    print(refresh_token)

    return access_token, refresh_token

def verify_access_token(token: str) -> str:
    """
    :param token: Access Token
    :return: ID użytkownika (jeśli token jest ważny)
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload["sub"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise Exception("Access Token has expired")
    except jwt.InvalidTokenError as e:
        print(f"aha? {e}")
        raise Exception("Invalid Access Token")
    
generate_tokens('6')
verify_access_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2IiwiZXhwIjoxNzM2MTYzOTc0LCJpYXQiOjE3MzYxNjAzNzR9.knlCv5UHzvDINZTBg7hWSotrpOWEEEMBCpviRJEbv-U')
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2IiwiZXhwIjoxNzM2MTYzNzAwLCJpYXQiOjE3MzYxNjAxMDB9.iIi_Lfk2FtVUSQ-1d-R9FjcWCPRosL3_Taz78iNfOyI
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjYsImV4cCI6MTczNjE2MzQ4OCwiaWF0IjoxNzM2MTU5ODg4fQ.Zcd3zUSDQRNYYSu8Dh95a552zdCoPIZVe7RoSEw_qN8