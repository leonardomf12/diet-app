import pandas as pd

from src.food_utils import load_food_db
from dash import dcc, html, dash_table

class DietApp:
    def __init__(self):

        self.food_db = load_food_db()


    def get_layout(self):
        return html.Div([
                dcc.Tabs([
                    dcc.Tab(label='Food Table', children=self.get_food_tab()),
                    dcc.Tab(label='Weekly Plan', children=self.get_weekly_tab())
                ]),
            ])
    def get_food_tab(self):
        food_table = []
        for food in self.food_db:
            row = food.get()
            food_table.append(row)
        # Dataframe
        df_food = pd.DataFrame(food_table)


        # Plotly Table
        table = dash_table.DataTable(
            data=df_food.to_dict('records'),  # Data for rows
            columns=[{'name': i, 'id': i} for i in df_food.columns],  # Column headers
            page_size=5,  # Number of rows per page (pagination)
            sort_action='native',  # Enable sorting by clicking headers
            filter_action='native'  # Enable filtering by columns
        )

        return table

    def get_weekly_tab(self):
        return []


