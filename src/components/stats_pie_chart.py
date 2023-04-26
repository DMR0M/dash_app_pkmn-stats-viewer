from dash import dcc
# import dash_bootstrap_components as dbc
import plotly.express as px
# ids
from . import ids
# data
from data.data import stats_data


def render(pkmn_name='Pikachu', *, pkmn_df=stats_data()) -> dcc.Graph:
    pkmn_name = pkmn_name.title()
    stats_data = pkmn_df.loc[pkmn_name][::-1]
    stats_labels = pkmn_df.columns.to_list()
    
    # Create initial pie chart
    stats_pie_fig = px.pie(stats_data, values=stats_data[stats_labels], names=stats_labels,
                    hole=0.3)
    
    # Return the pie chart figure
    graph = dcc.Graph(figure=stats_pie_fig, id=ids.STATS_PIE)
    return graph