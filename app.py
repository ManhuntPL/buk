import requests
from datetime import datetime

# Klucz API i adres backendu
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"
BASE_URL = "https://buk-wzmy.onrender.com"

# Funkcja do pobierania dzisiejszych meczów z wybranych lig

def get_today_matches(league_ids):
    today = datetime.today().strftime("%Y-%m-%d")
    endpoint = f"{BASE_URL}/matches"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    matches = []
    for league_id in league_ids:
        params = {
            "date": today,
            "league": league_id,
            "season": 2024
        }
        response = requests.get(endpoint, headers=headers, params=params)
        if response.status_code == 200:
            league_matches = response.json()
            matches.extend(league_matches.get("data", []))
        else:
            print(f"Błąd pobierania meczów dla ligi {league_id}: {response.status_code}")
    return matches

# Funkcja do pobierania wyników drużyn z całego sezonu

def get_team_results(team_id, season):
    endpoint = f"{BASE_URL}/results"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "team": team_id,
        "season": season
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Błąd pobierania wyników dla drużyny {team_id}: {response.status_code}")
        return []

# Funkcja do pobierania kursów dla meczów

def get_odds_for_match(match_id):
    endpoint = f"{BASE_URL}/odds"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "match": match_id
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Błąd pobierania kursów dla meczu {match_id}: {response.status_code}")
        return []

# Funkcja główna

def main():
    league_ids = [39, 135, 140, 61, 78]  # ID lig
    season = 2024

    # Pobieranie dzisiejszych meczów
    matches = get_today_matches(league_ids)
    print(f"Dzisiejsze mecze: {len(matches)}")

    for match in matches:
        home_team = match["homeTeam"]["name"]
        away_team = match["awayTeam"]["name"]
        match_id = match["id"]
        home_team_id = match["homeTeam"]["id"]
        away_team_id = match["awayTeam"]["id"]

        print(f"\nMecz: {home_team} vs {away_team}")

        # Forma drużyn
        home_results = get_team_results(home_team_id, season)
        away_results = get_team_results(away_team_id, season)
        print(f"Forma {home_team}: {len(home_results)} meczów")
        print(f"Forma {away_team}: {len(away_results)} meczów")

        # Pobieranie kursów
        odds = get_odds_for_match(match_id)
        if odds:
            print(f"Kursy dla meczu {home_team} vs {away_team}: {odds}")
        else:
            print("Brak danych o kursach")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def run_main():
        main()
        return "Dane zostały zaktualizowane."

    app.run(host="0.0.0.0", port=port)

