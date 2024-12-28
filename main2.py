import IPython
import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd

options = [{"label": "Tag1", "value": "Tag1"}, {"label": "Tag2", "value": "Tag2"},
           {"label": "Tag3", "value": "Tag3"}, {"label": "Tag4", "value": "Tag4"},
           {"label": "Tag5", "value": "Tag5"}, {"label": "Tag6", "value": "Tag6"}]
options_checklist = [{"label": "", "value": "selected"}]

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28],
    "Country": ["USA", "Canada", "UK"]
}
df = pd.DataFrame(data)

# Dash App
app = dash.Dash(__name__)

# Function to Generate Table
def generate_table(dataframe):
    columns = [""] + list(dataframe.columns) + ["Tags"] #First column is the Selection one
    rows = []
    for index, row in dataframe.iterrows():
        row_list = [dcc.Checklist(options=options_checklist, id=f"select-{index}")] + row.tolist() + [dcc.Dropdown(options=options, multi=True)]
        rows.append(row_list)

    # Post Processing to load as a Table
    columns = html.Thead(html.Tr([html.Th(col) for col in columns]))
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            rows[i][j] = html.Td(item)
        rows[i] = html.Tr(rows[i])
    rows = html.Tbody(children=rows)

    return html.Table([columns, rows])

# Layout
app.layout = html.Div([
    html.H1("Dynamic HTML Table from DataFrame"),
    generate_table(df)  # Call the function to generate the table
])

# Run App
if __name__ == "__main__":
    app.run_server(debug=True)
