from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Twój klucz API
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"
BASE_URL = "https://v3.football.api-sports.io"

# Endpoint: Aktualne tabele ligowe
@app.route('/standings', methods=['GET'])
def get_standings():
    league = request.args.get('league')
    season = request.args.get('season')
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    response = requests.get(f"{BASE_URL}/standings", headers=headers, params={"league": league, "season": season})
    return jsonify(response.json())

# Endpoint: Wyniki z aktualnego sezonu
@app.route('/results', methods=['GET'])
def get_results():
    league = request.args.get('league')
    season = request.args.get('season')
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    response = requests.get(f"{BASE_URL}/fixtures", headers=headers, params={"league": league, "season": season, "status": "FT"})
    return jsonify(response.json())

# Endpoint: Kursy bukmacherskie
@app.route('/odds', methods=['GET'])
def get_odds():
    league = request.args.get('league')
    season = request.args.get('season')
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    response = requests.get(f"{BASE_URL}/odds", headers=headers, params={"league": league, "season": season})
    return jsonify(response.json())

# Endpoint: Nadchodzące mecze w ciągu 7 dni
@app.route('/upcoming', methods=['GET'])
def get_upcoming():
    league = request.args.get('league')
    season = request.args.get('season')
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    params = {
        "league": league,
        "season": season,
        "from": request.args.get('from'),
        "to": request.args.get('to')
    }
    response = requests.get(f"{BASE_URL}/fixtures", headers=headers, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
