import json
def format_track_query(track):
    """
    Formats the track query for searching on Spotify.

    Args:
        track (dict): A dictionary containing track details.

    Returns:
        str: The formatted query string.
    """
    return f"{track['title']} {track['artist']['name']}"

def get_access_token(token_file):
    """
    Reads the access token from the given token file.

    Args:
        token_file (str): The path to the token file.

    Returns:
        str: The access token.
    """
    try:
        with open(token_file, 'r') as file:
            tokens = json.load(file)
            return tokens.get('access_token')
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading access token: {e}")
        return None