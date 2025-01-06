import os
from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "53e707bd6fcfd4e60ba0f74dc9a708c1"
    }

conn.request("GET", "/standings?league=39&season=2019", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
