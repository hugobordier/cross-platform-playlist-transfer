from deezer import get_deezer_playlist
#from spotify import create_spotify_playlist, search_spotify_track, add_tracks_to_spotify_playlist
#from utils import format_track_query

def main():
    playlist_data = get_deezer_playlist()
    if playlist_data:
        print("Playlist JSON Data:")
        print(playlist_data)
#        with open('playlist.json', 'w') as file:
#            import json
#            json.dump(playlist_data, file, indent=4)
#        print("Playlist JSON data has been written to 'playlist.json'.")
#   else:
#        print("Failed to fetch playlist data.")

if __name__ == "__main__":
    main()