import dash
from dash import html, dcc
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28],
    "Country": ["USA", "Canada", "UK"]
}
df = pd.DataFrame(data)

# Options for Dropdown and Checklist (example)
options = [{"label": "Tag1", "value": "Tag1"}, {"label": "Tag2", "value": "Tag2"},
           {"label": "Tag3", "value": "Tag3"}, {"label": "Tag4", "value": "Tag4"},
           {"label": "Tag5", "value": "Tag5"}, {"label": "Tag6", "value": "Tag6"}]

options_checklist = [{"label": "", "value": "selected"}]  # Example Checklist options (empty)

# Dash App
app = dash.Dash(__name__)

# Function to Generate Table
def generate_table(dataframe):
    columns = [""] + list(dataframe.columns) + ["Tags"]  # First column is for selection
    rows = []

    # Build the table rows
    for index, row in dataframe.iterrows():
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
            *[html.Td(row[col], style={'height': '100%', 'width': '100%'}) for col in dataframe.columns],  # Data columns
            html.Td(
                dcc.Dropdown(options=options, multi=True, id=dropdown_id, style={
                    'width': '200px',  # Fixed width for Dropdown
                    'minWidth': '200px',  # Prevent shrinking
                    'maxWidth': '200px'   # Prevent expanding
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
                children=[html.Tr(children=[html.Th(col, style={'fontWeight': 'bold', 'textAlign': 'center', 'padding': '10px'}) for col in columns])]
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

# Layout
app.layout = html.Div(
    children=[
        html.H1("Styled HTML Table from DataFrame", style={'textAlign': 'center'}),
        generate_table(df)  # Call the function to generate the table
    ],
    style={
        'overflowX': 'auto',  # Prevent horizontal scrolling due to table size changes
        'maxWidth': '100%'  # Prevent outer div from expanding
    }
)

# Run App
if __name__ == "__main__":
    app.run_server(debug=True)
