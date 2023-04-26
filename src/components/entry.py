from dash import html
import dash_bootstrap_components as dbc
# ids
from . import ids
# data
from data.data import category_data
# images
from scraper.img_scraper import find_image


def render(pkmn_name='Pikachu', *, pkmn_df=category_data()):
    pkmn_info = pkmn_df.loc[pkmn_name]
    info_list =  pkmn_info.to_list()
    
    # Filter info_list variable
    # FROM: ['#00025', "['Electric', nan]", 'Static Lightning Rod']
    # TO: ['#00025', "'Electric', nan", 'Static Lightning Rod']
    
    info_list = (
                 '|'.join(info_list)
                 .replace('[', '')
                 .replace(']', '')
                 .replace("'", "")
                 .replace('nan', '')
                 .split('|')
                )
    
    # print(info_list)
    dex_num, types, abilities = info_list
    
    # download the image
    find_image(pkmn_name)
    
    return (
        dbc.Container([
            html.Img(
                src=f'assets/pokemon/{pkmn_name.lower()}.jpg',
                alt=pkmn_name,
                width='20%', height='20%',
                style={
                    'float': 'left',
                    'margin': '10px',
                    'margin-left': '100px',
                }
            ),
            html.H3(
                f'Pokedex Number:',
                style={'text-align': 'right',}
            ),
            html.H3(
                f'{dex_num}',
                style={'margin-bottom': '40px',
                       'text-align': 'right'}
            ),
            html.H3(
                f'Type:',
                style={'text-align': 'right'}
            ),
            html.H3(
                f'{types}',
                style={'margin-bottom': '40px',
                       'text-align': 'right'}
            ),
            html.H3(
                f'Abilities:',
                style={'text-align': 'right'}
            ),
            html.H3(
                f'{abilities}',
                style={'margin-bottom': '40px',
                       'text-align': 'right'}
            )
            ], id=ids.PKMN_INFO,
        )
    )


