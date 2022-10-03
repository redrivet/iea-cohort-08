import requests


def get_joke():
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    if response.status_code != 200:
        joke_id = None
        joke = ''
    else:
        data = response.json()
        joke_id = data.get('id')
        joke = data.get('joke', '')
    return joke_id, joke
