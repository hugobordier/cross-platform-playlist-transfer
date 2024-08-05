import requests
from config import TOKEN_FILE, SPOTIFY_USER_ID
from utils import get_access_token

def create_spotify_playlist(name, description):
    """
    Creates a new playlist on Spotify.

    Args:
        name (str): The name of the new playlist.
        description (str): The description of the new playlist.

    Returns:
        str: The ID of the created playlist.
    """
    access_token = get_access_token(TOKEN_FILE)
    if not access_token:
        raise ValueError("No access token available")

    url = f'https://api.spotify.com/v1/users/{SPOTIFY_USER_ID}/playlists'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': name,
        'description': description,
        'public': False
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['id']

def search_spotify_track(query):
    """
    Searches for a track on Spotify.

    Args:
        query (str): The search query string.

    Returns:
        str: The Spotify track ID if found, else None.
    """
    access_token = get_access_token(TOKEN_FILE)
    if not access_token:
        raise ValueError("No access token available")

    url = f'https://api.spotify.com/v1/search?q={query}&type=track'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()
    if search_results['tracks']['items']:
        return search_results['tracks']['items'][0]['id']
    return None

def add_tracks_to_spotify_playlist(playlist_id, track_ids):
    """
    Adds tracks to a Spotify playlist.

    Args:
        playlist_id (str): The ID of the Spotify playlist.
        track_ids (list): A list of Spotify track IDs to add.

    Returns:
        None
    """
    access_token = get_access_token(TOKEN_FILE)
    if not access_token:
        raise ValueError("No access token available")

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'uris': [f'spotify:track:{track_id}' for track_id in track_ids]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
