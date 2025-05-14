
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def read_game(request: Request):
    return templates.TemplateResponse("game.html", {"request": request, "result": None})

@router.post("/", response_class=HTMLResponse)
def play_game(request: Request, player_choice: str = Form(...)):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "Draw!"
    elif (player_choice == "rock" and computer_choice == "scissors") or          (player_choice == "scissors" and computer_choice == "paper") or          (player_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"

    return templates.TemplateResponse("game.html", {
        "request": request,
        "result": result,
        "player_choice": player_choice,
        "computer_choice": computer_choice
    })
