from dash import dcc, dash_table
import plotly.express as px
# ids
from . import ids
# data
from data.data_handler import all_data


def render(*, pkmn_df=all_data()):
    return (
        dash_table.DataTable(pkmn_df)
    )
    