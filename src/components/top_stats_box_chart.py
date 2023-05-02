from dash import dcc
import plotly.express as px
# ids
from . import ids
# data
from data.data_grouper import group_by_stat


def render(stat='Hp', *, pkmn_df=group_by_stat):
    top_stat_pokemons = pkmn_df(stat)

    top_boxchart = px.box(top_stat_pokemons, points='all')
    top_boxchart.update_layout(
            # plot_bgcolor='rgba(0,0,0,0)',
            # paper_bgcolor='rgba(0,0,0,0)',
            xaxis_title='Stats',
            yaxis_title='Stat Range',
    )
    top_boxchart.update_xaxes(tickfont=dict(size=16))
    graph = dcc.Graph(figure=top_boxchart, id=ids.TOP_STATS_BOXCHART)
    return graph
