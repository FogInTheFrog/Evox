from datetime import date
from fastapi import FastAPI

app = FastAPI()
app.counter = 0


@app.get("/")
def hi():
    today = date.today()
    return {"message": str(today.year)}


@app.get("/counter")
def counter():
    app.counter += 1
    return app.counter
