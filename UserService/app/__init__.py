"""
Pakiet `app` odpowiedzialny jest za obsługę mikroserwisu użytkowników w aplikacji Flashcards.
"""
from .main import app
from .services import database, rabbitmq
import os
from dotenv import load_dotenv

__all__ = ["app", "database", "rabbitmq"]

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
RABBITMQ_URL = os.getenv("RABBITMQ_URL")