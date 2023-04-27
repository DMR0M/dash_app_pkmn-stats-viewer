import requests
from pathlib import Path


img_source_url = 'https://img.pokemondb.net/artwork'


def find_image(pkmn_name='pikachu', *, dir_path='assets/pokemon', url=img_source_url):
    pkmn_name = (
                pkmn_name
                .lower()
                .replace(' ', '-')
                .replace(':', '')
                .replace('.', '')
    )
    img_file = Path(f'{pkmn_name}.jpg')
    
    # Check if a pokemon image is already downloaded
    if Path(dir_path / img_file).is_file():
        return
    
    else:    
        try:
            img_response = requests.get(f'{url}/{pkmn_name}.jpg')
            
            # Download the image file from the url request
            if img_response.status_code == 200:
                
                with open(f'{dir_path}/{pkmn_name}.jpg', 'wb') as img_file:
                    img_file.write(img_response.content)
                    
            else:
                print('An error occured, no such url')
                
        except requests.exceptions.HTTPError as http_error:
            print(f'HTTP error occurred: {http_error}')
            
        except requests.exceptions.ConnectionError as conn_error:
            print(f'Connection error occurred: {conn_error}')
            raise ConnectionError(conn_error, request=img_response.request)
        
        except requests.exceptions.Timeout as timeout_error:
            print(f'Timeout error occurred: {timeout_error}')
            
        except requests.exceptions.RequestException as request_exception:
            print(f'Other error occurred: {request_exception}')
        
    

if __name__ == '__main__':
    find_image('Sprigatito')
    