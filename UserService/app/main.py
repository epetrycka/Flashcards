from fastapi import FastAPI
from app.routes.user import router as user_router
from app.services.database import init_db

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
def read_root():
    return {"message" : "User Service is running"}