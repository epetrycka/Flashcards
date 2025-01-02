from fastapi import FastAPI, Depends
from app.services.database import get_db

app = FastAPI()

@app.get("/test-db")
async def test_db_connection(db=Depends(get_db)):
    return {"message": "Connected to the database successfully"}
