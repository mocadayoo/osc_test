import requests
import base64

def get_access_token(client_id, client_secret):
    data = {'grant_type': 'client_credentials'}
    headers = {'Authorization': 'Basic ' + (base64.b64encode((client_id + ':' + client_secret).encode())).decode()}

    resp = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

    if resp.ok:
        token = resp.json()['access_token']
        return token
