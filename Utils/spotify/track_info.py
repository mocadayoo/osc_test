import requests

def get_track_info(token, track_id):
    url = "https://api.spotify.com/v1/tracks/" + track_id
    headers = {
        "authorization": "Bearer " + token,
    }

    resp = requests.get(url, headers=headers)
    if resp.status_code < 300:
        return resp.json()