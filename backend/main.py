from typing import Union
from fastapi import FastAPI

# routes
from routes.kaban_routes import routes

app = FastAPI()

app.include_router(routes)

@app.get("/")
def read_root():
    return {"response": "HELLO API FLASK GSI GUATEMALA"}
