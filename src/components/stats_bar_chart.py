from dash import dcc
# import dash_bootstrap_components as dbc
import plotly.express as px
# ids
from . import ids
# data
from data.data_handler import stats_data


def render(pkmn_name='Pikachu', *, pkmn_df=stats_data()) -> dcc.Graph:
    pkmn_name = pkmn_name.title()
    stats_data = pkmn_df.loc[pkmn_name][::-1]
    base_total = sum(stats_data.values)

    # Create initial bar chart
    stats_bar_fig = px.bar(stats_data, orientation='h')
    stats_bar_fig.update_xaxes(range=[0, 230], tickfont=dict(size=16))
    stats_bar_fig.update_layout(
            # plot_bgcolor='rgba(0,0,0,0)',
            # paper_bgcolor='rgba(0,0,0,0)',
            title=f'Base Total: {base_total}',
            xaxis_title=None,
            yaxis_title=None,
            showlegend=False,
    )
    stats_bar_fig.update_traces(textfont=dict(color='black'))
    
    # Return the bar chart figure
    graph = dcc.Graph(figure=stats_bar_fig, id=ids.STATS_BAR)
    return graph
