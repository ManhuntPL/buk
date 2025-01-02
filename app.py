from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Twój klucz API
API_KEY = "53e707bd6fcfd4e60ba0f74dc9a708c1"
BASE_URL = "https://v3.football.api-sports.io"

@app.route('/fixtures', methods=['GET'])
def get_fixtures():
    league = request.args.get('league', default="39")  # Premier League (domyślnie)
    season = request.args.get('season', default="2023")  # Sezon

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    params = {"league": league, "season": season}

    response = requests.get(f"{BASE_URL}/fixtures", headers=headers, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.status_code, "message": response.text})

if __name__ == '__main__':
    app.run(debug=True)
