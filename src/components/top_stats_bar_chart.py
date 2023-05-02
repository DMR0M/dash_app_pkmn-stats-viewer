from dash import dcc
import plotly.express as px
# ids
from . import ids
# data
from data.data_grouper import group_by_stat


def render(stat='Hp', *, pkmn_df=group_by_stat):
    top_stat_pokemons = pkmn_df(stat)
    
    top_barchart = px.bar(top_stat_pokemons[::-1], orientation='h')
    top_barchart.update_layout(
            # plot_bgcolor='rgba(0,0,0,0)',
            # paper_bgcolor='rgba(0,0,0,0)',
            xaxis_title='Stat Distribution',
            yaxis_title='Pokemon',
    )
    top_barchart.update_yaxes(tickfont=dict(size=16))
    
    graph = dcc.Graph(figure=top_barchart, id=ids.TOP_STATS)
    return graph
