from fastapi import FastAPI
import requests
import os

API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"  # Twój klucz API-Football
BASE_URL = "https://v3.football.api-sports.io"

app = FastAPI()

headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

@app.get("/matches")
async def get_matches(league_id: int, season: int):
    url = f"{BASE_URL}/fixtures"
    params = {
        "league": league_id,
        "season": season
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

@app.get("/team-form")
async def get_team_form(team_id: int, season: int):
    url = f"{BASE_URL}/fixtures"
    params = {
        "team": team_id,
        "season": season,
        "last": 10  # ostatnie 10 meczów dla formy
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

@app.get("/odds")
async def get_odds(fixture_id: int):
    url = f"{BASE_URL}/odds"
    params = {
        "fixture": fixture_id
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
