import requests  # type: ignore
from config import DEEZER_PLAYLIST_ID, DEEZER_TOKEN

def get_deezer_playlist():
    """
    Fetches the playlist details from Deezer.

    Returns:
        dict: A dictionary containing playlist details.

    Raises:
        Exception: If the request to Deezer API fails or if the response does not contain expected data.
    """
    deezer_url = f'https://api.deezer.com/playlist/{DEEZER_PLAYLIST_ID}'
    
    try:
        response = requests.get(deezer_url)  #,headers={'Authorization': f'Bearer {DEEZER_TOKEN}'} 
        response.raise_for_status()       
        playlist_data = response.json()
        if 'tracks' not in playlist_data or 'data' not in playlist_data['tracks']:
            raise ValueError("Unexpected response format: Missing 'tracks' or 'data' key.")
        
        return playlist_data
        
    except requests.RequestException as e:
        print(f"An error occurred while fetching the playlist from Deezer: {e}")
        raise
    except ValueError as e:
        print(f"An error occurred due to unexpected response format: {e}")
        raise
