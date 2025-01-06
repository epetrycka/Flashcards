import os
from dotenv import load_dotenv

load_dotenv("../.env")

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRES_IN: int = int(os.getenv("ACCESS_TOKEN_EXPIRES_IN", 3600))
    REFRESH_TOKEN_EXPIRES_IN: int = int(os.getenv("REFRESH_TOKEN_EXPIRES_IN", 86400))
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in the environment")
    
    print(SECRET_KEY)

    if not ALGORITHM:
        raise ValueError("ALGORITHM is not set in the environment")
    
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is not set in the environment")
    
    if not ACCESS_TOKEN_EXPIRES_IN:
        raise ValueError("ACCESS_TOKEN_EXPIRES_IN is not set in the environment")
    
    if not REFRESH_TOKEN_EXPIRES_IN:
        raise ValueError("REFRESH_TOKEN_EXPIRES_IN is not set in the environment")

settings = Settings()