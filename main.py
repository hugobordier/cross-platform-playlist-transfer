# main.py

from deezer import get_deezer_playlist
from spotify import create_spotify_playlist, search_spotify_track, add_tracks_to_spotify_playlist
from utils import format_track_query

def main():
    """
    Main function to convert a Deezer playlist to Spotify.
    """
    # Get Deezer playlist
    deezer_data = get_deezer_playlist()
    tracks = deezer_data['tracks']['data']

    # Create Spotify playlist
    spotify_playlist_name = deezer_data['title']
    spotify_playlist_description = 'Playlist imported from Deezer'
    spotify_playlist_id = create_spotify_playlist(spotify_playlist_name, spotify_playlist_description)

    # Search and add tracks to Spotify playlist
    spotify_track_ids = []
    for track in tracks:
        query = format_track_query(track)
        spotify_track_id = search_spotify_track(query)
        if spotify_track_id:
            spotify_track_ids.append(spotify_track_id)

    if spotify_track_ids:
        add_tracks_to_spotify_playlist(spotify_playlist_id, spotify_track_ids)
        print(f"Playlist '{spotify_playlist_name}' created on Spotify successfully!")

if __name__ == '__main__':
    main()
