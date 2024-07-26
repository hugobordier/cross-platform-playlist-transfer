import json
from deezer import get_deezer_playlist
from spotify import create_spotify_playlist, search_spotify_track, add_tracks_to_spotify_playlist
from utils import format_track_query

def main():
    # Load Spotify access token from file
    try:
        with open('tokens.json', 'r') as file:
            tokens = json.load(file)
            spotify_token = tokens.get('access_token')
            if not spotify_token:
                raise ValueError("No access token found")
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading Spotify token: {e}")
        return

    # Fetch Deezer playlist
    try:
        deezer_playlist = get_deezer_playlist()
    except Exception as e:
        print(f"Error fetching Deezer playlist: {e}")
        return

    if 'title' not in deezer_playlist or 'description' not in deezer_playlist:
        print("Deezer playlist is missing required fields.")
        return

    playlist_name = deezer_playlist['title']
    playlist_description = deezer_playlist['description']
    
    # Create a new Spotify playlist
    try:
        playlist_id = create_spotify_playlist(playlist_name, playlist_description)
        print(f"Created Spotify playlist with ID: {playlist_id}")
    except Exception as e:
        print(f"Error creating Spotify playlist: {e}")
        return

    # Prepare to add tracks to Spotify playlist
    track_ids_to_add = []
    
    # Iterate through each track in Deezer playlist and add to Spotify
    for track in deezer_playlist['tracks']['data']:
        query = format_track_query(track)
        try:
            spotify_track_id = search_spotify_track(query)
            if spotify_track_id:
                track_ids_to_add.append(spotify_track_id)
            else:
                print(f"Track not found on Spotify: {query}")
        except Exception as e:
            print(f"Error searching for track '{query}': {e}")
    
    if track_ids_to_add:
        try:
            add_tracks_to_spotify_playlist(playlist_id, track_ids_to_add)
            print("Tracks successfully added to Spotify playlist.")
        except Exception as e:
            print(f"Error adding tracks to Spotify playlist: {e}")
    else:
        print("No tracks to add to Spotify playlist.")

if __name__ == '__main__':
    main()
