from flask import Flask, request, redirect, jsonify
import requests
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

CLIENT_ID = '2fac091806a94209a92261288666ec3c'
CLIENT_SECRET = '58f69499d8f8428cb77de824eb2bc9d2'
REDIRECT_URI = 'http://localhost:8888/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
SCOPE = 'playlist-modify-public playlist-modify-private'
TOKEN_FILE = 'tokens.json'

@app.route('/')
def home():
    auth_url = (f"{AUTH_URL}?response_type=code&client_id={CLIENT_ID}&scope={SCOPE}"
                f"&redirect_uri={REDIRECT_URI}")
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Error: No code provided", 400

    response = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}", response.status_code

    response_data = response.json()
    access_token = response_data.get('access_token')
    refresh_token = response_data.get('refresh_token')

    if not access_token:
        return "Error: No access token found in the response", 400

    with open(TOKEN_FILE, 'w') as file:
        json.dump({
            'access_token': access_token,
            'refresh_token': refresh_token
        }, file)

    return jsonify({
        'access_token': access_token
    })

@app.route('/refresh_token')
def refresh_token():
    with open(TOKEN_FILE, 'r') as file:
        tokens = json.load(file)

    refresh_token = tokens.get('refresh_token')
    if not refresh_token:
        return "Error: No refresh token found", 400

    response = requests.post(TOKEN_URL, data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}", response.status_code

    response_data = response.json()
    access_token = response_data.get('access_token')

    if not access_token:
        return "Error: No access token found in the response", 400

    with open(TOKEN_FILE, 'w') as file:
        json.dump({
            'access_token': access_token,
            'refresh_token': refresh_token
        }, file)

    return jsonify({
        'access_token': access_token
    })

if __name__ == '__main__':
    app.run(port=8888)
