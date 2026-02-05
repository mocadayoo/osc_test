import requests
from urllib.parse import quote

def get_lryics(token, track_id, image_url):
    url = f"https://spclient.wg.spotify.com/color-lyrics/v2/track/{track_id}/image/{quote(image_url, safe='')}?format=json&vocalRemoval=false&market=from_token"
    headers = {
        "authorization": "Bearer " + token,
    }
    print(url)

    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    if resp.status_code < 300:
        return resp.json()