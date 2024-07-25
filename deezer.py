import requests
from config import DEEZER_PLAYLIST_ID, DEEZER_TOKEN

def get_deezer_playlist():
    """
    Fetches the playlist details from Deezer.

    Returns:
        dict: A dictionary containing playlist details.
    """
    deezer_url = f'https://api.deezer.com/playlist/{DEEZER_PLAYLIST_ID}'
    response = requests.get(deezer_url)
    response.raise_for_status()
    return response.json()