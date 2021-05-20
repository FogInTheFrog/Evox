from datetime import date
from fastapi import FastAPI
from .views import router as api_router

app = FastAPI()

# app.include_router(api_router)


@app.get("/")
def hi():
    today = date.today()
    return {"Hello, today is": str(today.year)}