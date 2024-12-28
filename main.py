import dash
from dash import dcc, html, Input, Output, State
import dash_table
import pandas as pd
import sqlalchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os
import IPython

# Initialize the Dash app


class DietApp(dash.Dash):
    def __init__(self, name):
        super().__init__(name)


        self.engine = self.get_db_engine()
        self.df = self.get_df_foods()
        self.tags = self.get_tags()

        self.layout = self.layout_

    @staticmethod
    def get_db_engine():
        db_username = os.getenv("DATABASE_USER")
        db_password = os.getenv("DATABASE_PASSWORD")
        db_host = "localhost"
        db_port = 5432
        db_name = os.getenv("DATABASE_NAME")

        return sqlalchemy.create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

    def get_df_foods(self):
        query = text("SELECT * FROM foods")
        return pd.read_sql(query, self.engine)

    def run_server(self, debug=False):
        if debug:
            super().run_server(debug=debug, host="0.0.0.0", port=8080)
        else:
            super().run_server(debug=debug, host="0.0.0.0", port=8080)

    # Additional help functions
    @staticmethod
    def get_tags():
        return [
            {"label": "Meat", "value": "Meat"},
            {"label": "Vegetal", "value": "Vegetal"},
            {"label": "Topping", "value": "Topping"},
            {"label": "Fruit", "value": "Fruit"}
        ]

    # Layout Functions
    def layout_(self):
        return html.Div(children=[
            html.H1("Diet Planner App"),
            dcc.Tabs(children=[
                dcc.Tab(id="tab-food-list", label="Food List", children=self.df_to_html_table()),
                dcc.Tab(id="tab-food-plan", label = "Diet Planner", children=html.Div("In progress"))
            ])
            ]
        )

    def df_to_html_table(self):
        """
        :param df: A Dataframe that will be converted to an HTML table with a select column first and a Tags column last
        :return:
        """
        options_checklist = [{"label": "", "value": True}]


        columns = [""] + list(self.df.columns) + ["Tags"]  # First column is for selection
        rows = []
        # Build the table rows
        for index, row in self.df.iterrows():
            checklist_id = f"select-{index}"
            dropdown_id = f"tags-{index}"
            # Alternating row background color
            row_style = {
                'backgroundColor': '#f2f2f2' if index % 2 == 0 else '#ffffff',  # Alternate colors
                'height': '100%',  # Make the row stretch
            }
            row_list = [
                html.Td(
                    dcc.Checklist(options=options_checklist, id=checklist_id),
                    style={
                        'display': 'flex',
                        'alignItems': 'center',
                        'justifyContent': 'center',
                        'height': '100%',  # Make Td stretch
                        'width': '100%',  # Make Td stretch
                    }
                ),  # Checklist column with dynamic ID
                *[html.Td(row[col], style={'height': '100%', 'width': '100%'}) for col in self.df.columns],
                # Data columns
                html.Td(
                    dcc.Dropdown(options=self.tags, multi=True, id=dropdown_id, style={
                        'width': '200px',  # Fixed width for Dropdown
                        'minWidth': '200px',  # Prevent shrinking
                        'maxWidth': '200px'  # Prevent expanding
                    })  # Tags column with dynamic ID
                )
            ]
            rows.append(html.Tr(
                row_list,
                style=row_style  # Apply alternating row color style
            ))  # Create a row for the table
        # Build the table with styling
        table = html.Table(
            children=[
                # Header
                html.Thead(
                    children=[html.Tr(
                        children=[html.Th(col, style={'fontWeight': 'bold', 'textAlign': 'center', 'padding': '10px'})
                                  for col in columns])]
                ),
                # Body
                html.Tbody(children=rows)
            ],
            style={
                'border': '1px solid black',  # Border around the table
                'borderCollapse': 'collapse',  # Collapse borders between cells
                'width': '80%',  # Adjust table width
                'margin': 'auto',  # Center the table
                'textAlign': 'center',  # Center text in the table
                'tableLayout': 'fixed'  # Ensures fixed table width
            }
        )
        return table


class Food:
    def __init__(self, food_name:str, calories: float, carbs: float, protein: float, fat: float, unit):
        self.food_name = food_name
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.unit = unit

        self.engine = self.get_db_engine()


    @staticmethod
    def get_db_engine():
        db_username = os.getenv("DATABASE_USER")
        db_password = os.getenv("DATABASE_PASSWORD")
        db_host = "localhost"
        db_port = 5432
        db_name = os.getenv("DATABASE_NAME")

        return sqlalchemy.create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

    def save(self):
        with self.engine.connect() as conn:
            query = text("""
                INSERT INTO foods (name, calories, protein, fat, carbs, unit)
                VALUES (:name, :calories, :protein, :fat, :carbs, :unit)
            """)

            conn.execute(query, {
                'name': self.food_name,
                'calories': self.calories,
                'protein': self.protein,
                'fat': self.fat,
                'carbs': self.carbs,
                'unit': self.unit
            })
            conn.commit()
        print(f"Food: {self.food_name} saved sucessfully!")

    def delete(self):
        with self.engine.connect() as conn:
            query = text("""
                DELETE FROM foods
                WHERE name = :name
            """)

            conn.execute(query, {
                'name': self.food_name,
            })
            conn.commit()
        print(f"Food: {self.food_name} deleted sucessfully!")



# Run the app
if __name__ == '__main__':
    load_dotenv(dotenv_path='.env')

    app = DietApp(__name__)
    app.run_server(debug=True)

    #app.run_server(debug=True)
