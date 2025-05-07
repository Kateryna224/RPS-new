from typing import Literal
from fastapi import FastAPI, Query
import random
from pydantic import BaseModel
import uvicorn

from enum import Enum


app = FastAPI()


class Choice(str, Enum):
    КАМЕНЬ = "камень"
    БУМАГА = "бумага"
    НОЖНИЦЫ = "ножницы"

Winner = Literal['КОМПЬЮТЕР', 'ИГРОК', 'НИЧЬЯ']

class GameResponse(BaseModel):
    player_choice: Choice
    computer_choice: Choice
    winner: Winner


WINNING_COMBINATIONS = {
    Choice.КАМЕНЬ: Choice.НОЖНИЦЫ,
    Choice.БУМАГА: Choice.КАМЕНЬ,
    Choice.НОЖНИЦЫ: Choice.БУМАГА
}


def get_random_choice(choices: list[str]):
    return random.choice(choices)


def determine_winner(player_choice: Choice, computer_choice: Choice) -> Winner:
    if player_choice == computer_choice:
        return "Ничья"
    elif WINNING_COMBINATIONS[player_choice] == computer_choice:
        return "Игрок"
    else:
        return 'Компьютер'


@app.get("/", response_model=GameResponse)
def play(player_choice: Choice = Query(..., description="Выбери: камень, бумага или ножницы")):
    computer_choice = get_random_choice(Choice)
    winner = determine_winner(player_choice, computer_choice)

    return GameResponse(
        player_choice=player_choice,
        computer_choice=computer_choice,
        winner=winner
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
