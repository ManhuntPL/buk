from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Twój klucz API
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"
BASE_URL = "https://v3.football.api-sports.io"

# Lista ID topowych lig
TOP_LEAGUES = {
    "Premier League": "39",
    "Ligue 1": "61",
    "Bundesliga": "78",
    "Serie A": "135",
    "La Liga": "140"
}

# Endpoint: Wyniki z sezonu 2024 dla topowych lig
@app.route('/season_results', methods=['GET'])
def get_season_results():
    league = request.args.get('league')
    if league not in TOP_LEAGUES.values():
        return jsonify({"error": "Invalid league. Allowed leagues are Premier League, Ligue 1, Bundesliga, Serie A, La Liga."}), 400

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    params = {
        "league": league,
        "season": "2024",
        "status": "FT"
    }
    response = requests.get(f"{BASE_URL}/fixtures", headers=headers, params=params)
    return jsonify(response.json())

# Endpoint: Analiza danych pod kątem najbardziej prawdopodobnych wyników
@app.route('/analyze_match', methods=['GET'])
def analyze_match():
    league = request.args.get('league')
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    if league not in TOP_LEAGUES.values():
        return jsonify({"error": "Invalid league. Allowed leagues are Premier League, Ligue 1, Bundesliga, Serie A, La Liga."}), 400

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }

    # Wyniki z sezonu
    season_results = requests.get(f"{BASE_URL}/fixtures", headers=headers, params={
        "league": league,
        "season": "2024",
        "status": "FT"
    }).json()

    # Mecze bezpośrednie
    h2h = requests.get(f"{BASE_URL}/fixtures/headtohead", headers=headers, params={
        "h2h": f"{team1}-{team2}"
    }).json()

    # Kursy
    odds = requests.get(f"{BASE_URL}/odds", headers=headers, params={
        "league": league,
        "season": "2024"
    }).json()

    # Analiza (przykład uproszczony)
    analysis = {
        "team1": team1,
        "team2": team2,
        "recent_results": season_results["response"],
        "head_to_head": h2h["response"],
        "odds": odds["response"]
    }

    return jsonify(analysis)

# Endpoint: Lista topowych lig
@app.route('/leagues', methods=['GET'])
def get_allowed_leagues():
    return jsonify(TOP_LEAGUES)

if __name__ == '__main__':
    app.run(debug=True)
