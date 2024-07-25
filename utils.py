def format_track_query(track):
    """
    Formats the track query for searching on Spotify.

    Args:
        track (dict): A dictionary containing track details.

    Returns:
        str: The formatted query string.
    """
    return f"{track['title']} {track['artist']['name']}"