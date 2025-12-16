from fastapi import FastAPI
from app.nba.stats import get_games

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/nba/games")
def games():
    return get_games()
