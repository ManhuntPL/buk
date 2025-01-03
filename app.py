import os
from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

# Klucz API-Football
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"
BASE_URL = "https://v3.football.api-sports.io/"

# Funkcja do pobierania danych z API-Football zgodnie z poprawnym formatem zapytania
def get_fixtures_for_today(league_ids):
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    today_date = datetime.today().strftime('%Y-%m-%d')
    fixtures = []

    for league_id in league_ids:
        params = {
            "league": league_id,
            "season": str(datetime.today().year),
            "date": today_date
        }
        response = requests.get(f"{BASE_URL}fixtures", headers=headers, params=params)
        data = response.json()

        # Obsługa odpowiedzi bez błędów
        if data.get("errors"):
            fixtures.append({"league_id": league_id, "error": data["errors"]})
        else:
            fixtures.extend(data.get("response", []))

    return {
        "get": "fixtures",
        "parameters": {
            "date": today_date,
            "leagues_checked": league_ids
        },
        "errors": [],
        "results": len(fixtures),
        "paging": {
            "current": 1,
            "total": 1
        },
        "fixtures": fixtures
    }

# Endpoint do strony głównej
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Football Fixtures API",
        "endpoints": {
            "/today-fixtures": "Get today's fixtures for top European leagues"
        }
    })

# Endpoint do pobierania meczów z dzisiejszego dnia
@app.route('/today-fixtures', methods=['GET'])
def get_today_fixtures():
    league_ids = [39, 135, 140, 61, 78]  # Premier League, Serie A, La Liga, Ligue 1, Bundesliga
    fixtures = get_fixtures_for_today(league_ids)
    return jsonify(fixtures)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
