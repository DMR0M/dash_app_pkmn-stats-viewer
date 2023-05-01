import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px

# src components
from src.components import ids
from src.components import stats_bar_chart
from src.components import stats_pie_chart
from src.components import stats_heat_map
from src.components import gen_histogram
from src.components import top_stats_bar_chart
from src.components import top_stats_box_chart
from src.components import entry

# data
from data.data_handler import stats_data


cols = stats_data().columns.to_list()

CSS_FILE = 'assets/logo.css'
app = dash.Dash(__name__, 
                external_scripts=['/assets/scripts/onEnterSearch.js'],
                external_stylesheets=CSS_FILE)


app = Dash(external_stylesheets=[dbc.themes.JOURNAL])
app.title = 'Pokemon Stats Viewer'


header_title = dcc.Markdown(children='Pokemon Stats Viewer')
app.layout = html.Div([
    html.Div(children=[
        html.Link(rel='stylesheet', href='assets/style.css'),
        html.Img(className='logo-class', src='assets/pokeball.png',
                     style={'padding': '1px',
                            'height': '40px',
                            'width': '40px',
                            'margin-right': '15px',}
                    ),
            html.H1(className='main-app-title', children=header_title,
                    style={'text-align': 'center',
                           'margin-top': '20px',
                           }),
        ], style={'display': 'flex',
                  'justify-content': 'center',
                  'align-items': 'center',
                  'heignt': '100vh'}),
        html.Br(),
        dbc.Container(html.Div([
            html.A('See list of Pokemon here', href='https://pokemondb.net/pokedex/national'),
        ])),
        html.Hr(),
        html.Br(),
        dbc.Container(
        html.Div([
            dcc.Input(id='pkmn-search-input', type="text", placeholder="Search by Pokemon name", 
                  value='Pikachu',
                  # Input Field Flags
                  # ----------------------------------------------------------------
                  debounce=True,
                  autoComplete='on',
                  # ----------------------------------------------------------------
                  style={
                      'width': '70%',
                      'height': '45px',
                      'display': 'inline-block',
                      'text-align': 'center',
                      'margin-right': '15px',
                      'border': '2px solid',
                    }
                ),
            dbc.Button('Search', id='pkmn-search-btn', n_clicks=0,
                   style={
                       'width': '25%',
                       'height': '45px',
                       'display': 'inline-block',
                    #    'margin-left': '15px',
                       'text-align': 'center',
                       'float': 'right',
                    }
                ),
            html.Br(),
            html.Br(),
            html.Hr(),
            html.H2(id='pkmn-name-label', style={'text-align': 'center'}),
            # html.Img(src='assets/pokeball.png')
            
        ])
        ),
        dbc.Container([
            entry.render(),
        ], style={
            'margin': '80px',
        }),
        stats_bar_chart.render(),
        stats_pie_chart.render(),
        html.Hr(),
        html.H2('Top 10 Pokemon with the Highest Selected Stat',
                style={
                        'margin': '10px', 
                }),
        html.Hr(),
        dcc.Dropdown(
            cols,
            value=cols[0],
            id='stats-dropdown',
            style={
                'border': '2px solid #ccc',
                'border-radius': '4px'
            },
        ),
        html.Hr(),
        html.H2('Bar Chart',
                style={
                        'margin': '10px', 
                        'text-align': 'center',
                }),
        html.Hr(),
        top_stats_bar_chart.render(),
        html.Hr(),
        html.H2('Box Plot',
                style={
                        'margin': '10px', 
                        'text-align': 'center',
                }),
        html.Hr(),
        top_stats_box_chart.render(),
        html.Hr(),
        html.H2('Number of each Pokemon for each generation',
                style={
                        'margin': '10px', 
                        'text-align': 'center',
                }),
        html.Hr(),
        gen_histogram.render(),
        dbc.Container(
            style={
                'display': 'flex',
                'justify-content': 'center',
                'align-items': 'center',
			    'height': '100vh',
            },
            children=[
                stats_heat_map.render(),
                # data_table.render(),
        ]),
    ])
    
    
@app.callback(
    [Output(stats_bar_chart.render().id, 'figure'), Output(stats_pie_chart.render().id, 'figure'),
     Output('pkmn-name-label', 'children'), Output(entry.render().id, 'children'),],
    [Input('pkmn-search-btn', 'n_clicks')],
    [State('pkmn-search-input', 'value'),
     State(stats_bar_chart.render().id, 'figure'), State(stats_pie_chart.render().id, 'figure')]
)
def update_charts(_, value, bar_fig, pie_fig):
    value = value.title()
    
    if value not in stats_data().index.to_list():
        bar_fig = px.bar()
        bar_fig.update_xaxes(range=[0, 230], tickfont=dict(size=16))
        bar_fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
        )
        pie_fig = px.pie()
        info_container = html.Div([
            html.H3(
                style={'display': 'inline-block',
                       'margin-bottom': '15px'}
            ),
            html.H4(
                f'Pokedex Number:',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            ),
            html.H3(
                f'NO DATA FOUND',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            ),
            html.H4(
                f'Type:',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            ),
            html.H3(
                f'NO DATA FOUND',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            ),
            html.H4(
                f'Abilities:',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            ),
            html.H3(
                f'NO DATA FOUND',
                style={'text-align': 'left',
                       'margin-bottom': '15px'}
            )
            ], id=ids.PKMN_INFO,
        )
        # Return empty charts   
        return bar_fig, pie_fig, 'NO DATA FOUND', info_container
    
    # Set an initial state for the bar chart and pie chart
    bar_fig = stats_bar_chart.render(value).figure
    bar_fig.update_xaxes(range=[0, 230], tickfont=dict(size=16))
    bar_fig.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
    )
    # bar_fig.update_traces(textfont=dict(color='black'))
    
    pie_fig = stats_pie_chart.render(value).figure
    
    pkmn_info = entry.render(value)
    
    return bar_fig, pie_fig, value, pkmn_info


app.clientside_callback(
    # Javascript function
    'onEnterSearchPress',
    [Output('pkmn-search-input', 'value'),],
    [Input('pkmn-search-btn', 'n_clicks'),],
    [State('pkmn-search-input', 'value'),],
)


@app.callback(
    [Output(top_stats_bar_chart.render().id, 'figure'),
     Output(top_stats_box_chart.render().id, 'figure'),],
    [Input('stats-dropdown', 'value')],
)
def update_dropdown(stat_selection):
    bar_top_stats = top_stats_bar_chart.render(stat_selection).figure
    box_top_stats = top_stats_box_chart.render(stat_selection).figure
    return bar_top_stats, box_top_stats
    

if __name__ == '__main__':
    app.run_server(port=8501)
    
    