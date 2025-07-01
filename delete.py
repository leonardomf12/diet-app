from dash import Dash, html

app = Dash(__name__)

# Create 32 cells (4 rows × 8 columns)
def custom_cell(i):
    return html.Div(
        f"Cell {i+1}",
        style={
            "background": "#e0e0e0",
            "border": "1px solid #bbb",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "fontSize": "18px",
            "borderRadius": "6px"
        }
    )

grid_items = [custom_cell(i) for i in range(32)]

# Main layout with a full-page grid
app.layout = html.Div(
    style={
        "height": "50vh",  # Full viewport height
        "width": "100vw",   # Full viewport width
        "display": "grid",
        "gridTemplateColumns": "repeat(8, 1fr)",  # 8 flexible columns
        "gridTemplateRows": "repeat(4, 1fr)",     # 4 flexible rows
        "gap": "0px",
        "padding": "0px",
        "boxSizing": "border-box"
    },
    children=grid_items
)

if __name__ == "__main__":
    app.run(debug=True)
