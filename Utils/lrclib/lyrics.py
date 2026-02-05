import requests
from urllib.parse import quote

def get_lrc_lyrics(artist_name, track_name):
    url = f"https://lrclib.net/api/get?artist_name={artist_name}&track_name={track_name}"

    resp = requests.get(url)
    if resp.ok:
        return resp.json()