from deezer import get_deezer_playlist

def main():
    deezer_data = get_deezer_playlist()
    tracks = deezer_data['tracks']['data']
    if deezer_data:
        print("Playlist JSON Data:")
        print(tracks)

if __name__ == "__main__":
    main()