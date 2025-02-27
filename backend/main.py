from typing import Union
from fastapi import FastAPI

# routes
from routes.task import routes

app = FastAPI()

app.include_router(routes)

@app.get("/")
def read_root():
    return {"response": "HELLO API FLASK GSI GUATEMALA"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}