from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/")
def play(player_choice: str = Query(..., description="Выбери: камень, бумага или ножницы")):
    choices = ["камень", "бумага", "ножницы"]
    computer_choice = random.choice(choices)

    if (player_choice == "камень" and computer_choice == "ножницы") or \
       (player_choice == "ножницы" and computer_choice == "бумага") or \
       (player_choice == "бумага" and computer_choice == "камень"):
        winner = "Игрок"
    elif player_choice == computer_choice:
        winner = "Ничья"
    else:
        winner = "Компьютер"

    return {
        "Игрок выбрал": player_choice,
        "Компьютер выбрал": computer_choice,
        "Результат": winner
    }
