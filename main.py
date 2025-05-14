from typing import Literal
from fastapi import FastAPI, Query
import random
from pydantic import BaseModel
import uvicorn

from enum import Enum


app = FastAPI(
    title="Камень, ножницы, бумага",
    description="Сервис для игры в камень, ножницы, бумага",
    version="1.0.0",
    prefix="/api"
)

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}