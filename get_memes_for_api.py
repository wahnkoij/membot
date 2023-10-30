import requests
import json


def get_memes(url):
    response = json.loads(requests.get(url).text)

    images = {'img': []}
    for url in response:
        for key, val in url.items():
            if key == 'url':
                images['img'].append(val)

    with open('memes.json', 'w') as file:
        json.dump(images, file)
