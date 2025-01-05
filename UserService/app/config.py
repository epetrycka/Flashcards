import os
from dotenv import load_dotenv

load_dotenv("../.env")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
    WEBSOCKETS_URL = os.getenv("WEBSOCKETS_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in the environment")

settings = Settings()