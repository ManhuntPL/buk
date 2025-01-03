import os
from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Klucz API-Football
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"  # Twój klucz API-Football
BASE_URL = "https://v3.football.api-sports.io/"

# Funkcja do pobierania danych z API-Football
def get_fixtures_for_today(league_ids):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    today_date = datetime.today().strftime('%Y-%m-%d')
    fixtures = []

    for league_id in league_ids:
        params = {
            "date": today_date,
            "league": league_id,
            "season": datetime.today().year
        }
        response = requests.get(f"{BASE_URL}fixtures", headers=headers, params=params)
        data = response.json()
        if data.get("response"):
            fixtures.extend(data["response"])

    return fixtures

# Endpoint do pobierania meczów z dzisiejszego dnia
@app.route('/today-fixtures', methods=['GET'])
def get_today_fixtures():
    league_ids = [39, 135, 140, 61, 78]  # Premier League, Serie A, La Liga, Ligue 1, Bundesliga
    fixtures = get_fixtures_for_today(league_ids)
    return jsonify({"today_fixtures": fixtures})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
