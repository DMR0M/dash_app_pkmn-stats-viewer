from dash import dcc
# import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
# ids
from . import ids
# data
from data.data_handler import stats_data


# Create a heatmap of the correlation of all pokemon's stats 
def render(*, pkmn_df=stats_data()) -> dcc.Graph:
    correlation_df = pd.DataFrame(pkmn_df).corr()
    heat_map_chart = px.imshow(correlation_df, text_auto=True, 
                     width=800, height=800, 
                     title='All Pokemon Stats Correlations (Gen 1 - Gen 9)')
    
    # Export heatmap
    return dcc.Graph(figure=heat_map_chart, id=ids.CORR_HEAT_MAP)
