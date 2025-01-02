from fastapi import FastAPI
from app.services.database import create_tables
from app.routers.user import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/")
def root():
    return {"message" : "UserService is running"}