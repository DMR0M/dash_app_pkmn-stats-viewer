import requests
import io
from PIL import Image


img_source_url = 'https://img.pokemondb.net/artwork'


# Load an image from the web by PARAMETERIZED URL
def load_image(pkmn_name=None):
    if pkmn_name is None:
        raise ValueError('Parameter is not initialized')
    
    pkmn_image = f'{pkmn_name}.jpg'
    image_request = requests.get(f'{img_source_url}/{pkmn_image}')
        
    image_data = image_request.content
    return image_data
