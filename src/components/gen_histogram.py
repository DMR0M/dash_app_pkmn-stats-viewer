from dash import dcc
# import dash_bootstrap_components as dbc
import plotly.express as px
# ids
from . import ids
# data
from data.data_handler import distributed_data


def render(*, pkmn_df=distributed_data()) -> dcc.Graph:
    hist_chart = px.histogram(
        pkmn_df, 
        x='Generation', 
        # title='Number of Pokemon for each Generation',
        nbins=10,
        color_discrete_sequence=['indianred'],
    )
    hist_chart.update_layout(
        bargap=0.1,
        
        xaxis=dict
        (
            tickfont=dict(size=18),
            
        )
    )
    
    return dcc.Graph(figure=hist_chart, id=ids.GEN_HIST_GRAPH)
    