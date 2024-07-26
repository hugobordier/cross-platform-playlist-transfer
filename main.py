import requests
import json

TOKEN_FILE = 'tokens.json'

def get_access_token():
    try:
        with open(TOKEN_FILE, 'r') as file:
            tokens = json.load(file)
            return tokens.get('access_token')
    except FileNotFoundError:
        print("Token file not found. Please authenticate first.")
        return None

def refresh_access_token():
    response = requests.get('http://localhost:8888/refresh_token')
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        with open(TOKEN_FILE, 'r+') as file:
            tokens = json.load(file)
            tokens['access_token'] = access_token
            file.seek(0)
            json.dump(tokens, file)
        return access_token
    else:
        print("Failed to refresh token.")
        return None

def ensure_valid_token():
    access_token = get_access_token()
    if not access_token:
        print("Access token not available. Please authenticate.")
        return None
    
    # Optionally: Check if the token is expired here
    # For simplicity, assume the token is valid or use a token expiry check

    return access_token

def main():
    access_token = ensure_valid_token()
    if not access_token:
        access_token = refresh_access_token()
    
    if not access_token:
        print("Unable to get access token.")
        return

    # Use `access_token` for your API calls
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Example API call
    response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    print(response.json())

if __name__ == "__main__":
    main()
