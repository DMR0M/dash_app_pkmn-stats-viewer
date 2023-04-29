from dash import html
import dash_bootstrap_components as dbc
import base64

from . import ids
from data.data_handler import category_data
from loader.img_loader import load_image
# from scraper.img_scraper import find_image


def render(pkmn_name='Pikachu', *, pkmn_df=category_data(), img_loader=load_image):
    pkmn_info = pkmn_df.loc[pkmn_name]
    info_list =  pkmn_info.to_list()
    
    pkmn_name = (
        pkmn_name
        .lower()
        .replace(' ', '-')
        .replace(':', '')
        .replace('.', '')
    )
        
    # Get image of Pokemon
    pkmn_img_data = img_loader(pkmn_name)

    # Filter info_list variable
    # FROM: ['#00025', "['Electric', nan]", 'Static Lightning Rod']
    # TO: ['#00025', "'Electric', nan", 'Static Lightning Rod']
    # print(info_list)

    info_list = list(map(lambda x: str(x), info_list))
    info_list = (
                 '|'.join(info_list)
                 .replace('[', '')
                 .replace(']', '')
                 .replace("'", "")
                 .replace('nan', '')
                 .split('|')
                )
    
    # print(info_list)
    dex_num, types, abilities, gen = info_list
    
    # # download the image
    # find_image(pkmn_name)
    
    return (
        html.Div([
            html.Img(
                src=f'data:image/png;base64,{base64.b64encode(pkmn_img_data).decode()}',
                # src=f'assets/pokemon/{(pkmn_name.lower().replace(" ", "-").replace(".", "").replace(":", ""))}.jpg',
                alt=pkmn_name,
                style={
                    'float': 'right',
                    'width': '200px',
                    'heigth': '200px',
                    'border-radius': '2px',
                    # 'padding': '10px',
                    }
                ),
            html.H3(
                f'Pokedex Number:',
                style={'text-align': 'left',}
            ),
            html.H4(
                f'{dex_num}',
                style={'margin-bottom': '40px',
                       'text-align': 'left'}
            ),
            html.H3(
                f'Generation:',
                style={'text-align': 'left',}
            ),
            html.H4(
                f'{gen}',
                style={'margin-bottom': '40px',
                       'text-align': 'left'}
            ),
            html.H3(
                f'Type:',
                style={'text-align': 'left'}
            ),
            html.H4(
                f'{types}',
                style={'margin-bottom': '40px',
                       'text-align': 'left'}
            ),
            html.H3(
                f'Abilities:',
                style={'text-align': 'left'}
            ),
            html.H4(
                f'{abilities}',
                style={'margin-bottom': '40px',
                       'text-align': 'left'}
            )
            ], id=ids.PKMN_INFO,
            #    style={
            #        'margin': '40px',
            #    }
        )
    )


