import requests
import json

TOKEN_FILE = 'tokens.json'

def get_access_token():
    try:
        with open(TOKEN_FILE, 'r') as file:
            tokens = json.load(file)
            return tokens['access_token']
    except FileNotFoundError:
        print("Token file not found. Please authenticate first.")
        return None

def refresh_access_token():
    response = requests.get('http://localhost:8888/refresh_token')
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        with open(TOKEN_FILE, 'w') as file:
            json.dump({
                'access_token': access_token,
                'refresh_token': get_refresh_token()  # Ensure refresh token is saved too
            }, file)
        return access_token
    else:
        print("Failed to refresh token.")
        return None

def get_refresh_token():
    try:
        with open(TOKEN_FILE, 'r') as file:
            tokens = json.load(file)
            return tokens['refresh_token']
    except FileNotFoundError:
        print("Token file not found. Please authenticate first.")
        return None

def main():
    access_token = get_access_token()
    if not access_token:
        access_token = refresh_access_token()
    
    if not access_token:
        print("Unable to get access token.")
        return

    # Utilisez `access_token` pour vos appels API
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Exemple d'appel API
    response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    print(response.json())

if __name__ == "__main__":
    main()
