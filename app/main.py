
from fastapi import FastAPI
from app.routes import game, items

app = FastAPI(title="RPS CRUD", version="1.0.0")

app.include_router(game.router)
app.include_router(items.router)
