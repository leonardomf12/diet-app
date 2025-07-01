import pandas as pd

from src.food_utils import load_food_db
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

class DietApp:
    def __init__(self):
        self.days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.meals = ["Breakfast", "Morning Snack", "Lunch", "Afternoon Snack", "Dinner", "Supper"]

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

    def user_input_layout(self):
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H3("Days of the Week"),
                    dcc.Dropdown(options=self.days_week, id="Day-MultiSelect", multi=True, style={"width": "100%"}),
                    html.H3("Meals"),
                    dcc.Dropdown(options=self.meals, id="Meal-MultiSelect", multi=True, style={"width": "100%"}),
                ], width=4),
                dbc.Col([
                    dcc.Dropdown(options=[], id="Food-MultiSelect", multi=True, style={"width": "100%"}), #TODO options to all the foods
                ],width=6),
                dbc.Col([
                    dbc.Row([
                        dbc.Button("Add Food", id="Add-Food-Button", color="primary", n_clicks=0),
                        dbc.Button("Remove Food", id="Remove-Food-Button", color="primary", n_clicks=0),
                        dbc.Input(id="quantity-food", placeholder="Quantity", type="number"),
                    ])
                ], width=2, style={"background": "blue", "display": "flex", "justifyContent": "center",})
            ], className="gx-5", justify="center", style={"display": "flex", "alignItems": "center", "justifyContent": "center", "background": "#e0e0e0"})
        ], fluid=True)

    def weekly_layout(self):
        return []