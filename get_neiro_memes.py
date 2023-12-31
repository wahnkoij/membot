import openai
import json

api_key = 'your-api-key'


def get_neiro_memes():
    openai.api_key = api_key
    img = openai.Image.create(
        prompt='star wars memes', # you can change it or apply anything else
        n=2,
        size='512x512',
        response_format='url'
    )
    image = {'img': []}
    for url in img['data']:
        image['img'].append(url['url'])

    with open('neiro.json', 'w') as file:
        json.dump(image, file)

        
get_neiro_memes()
