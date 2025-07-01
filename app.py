import dash
from dash import dcc, html, dash_table
import pandas as pd

from src.html_components import DietApp
import dash_bootstrap_components as dbc

app_obj = DietApp()

app = dash.Dash(external_stylesheets=[dbc.themes.GRID])
app.layout = app_obj.weekly_layout
# app.layout = html.Div([
#     dcc.Tabs([
#         dcc.Tab(label='Food Table', children=[
#             dash_table.DataTable(
#                 id='food-table',
#                 columns=[{"name": i, "id": i} for i in df.columns],
#                 data=df.to_dict('records'),
#                 page_size=10,
#                 style_table={'overflowX': 'auto'},
#             )
#         ]),
#         dcc.Tab(label='Food Boxes', children=[
#             html.Div(
#                 style={'display': 'flex', 'flexDirection': 'row', 'height': '80vh', 'borderLeft': '1px solid black'},
#                 children=[
#                     html.Div(
#                         id=f'box-column-{i+1}',
#                         style={
#                             'flex': '1',
#                             'borderRight': '1px solid black' if i < 6 else 'none',  # vertical line except last division
#                             'padding': '10px',
#                             'overflowY': 'auto',
#                             'minWidth': '120px',
#                         },
#                         children=[
#                             html.H4(f'Division {i+1}'),
#                             # Insert your food boxes here
#                         ]
#                     ) for i in range(7)
#                 ]
#             )
#         ])
#     ])
# ])

if __name__ == '__main__':
    app.run(debug=True)
