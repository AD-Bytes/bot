import requests
import random

pokemon = random.randint(1, 1025)
def get_apokemon_img_url():    
    url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon}.png'
    res = requests.get(url)
    data = res.json()
    return data['url']

