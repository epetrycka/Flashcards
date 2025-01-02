#file config.py cannot be imported in database.py for unknown reasons

import os
from dotenv import load_dotenv

load_dotenv("../.env")

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set in the environment")

settings = Settings()