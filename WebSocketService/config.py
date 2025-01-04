import os
from dotenv import load_dotenv

load_dotenv(".env")

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    REFRESH_TOKEN_EXPIRE_DAYS = os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")
    SESSION_TIMEOUT = os.getenv("SESSION_TIMEOUT")

settings = Settings()