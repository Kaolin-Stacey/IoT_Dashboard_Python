import dash
from dash import html
import dash_bootstrap_components as dbc
from components import sidebar
from content import content

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1 rem"
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./styles/stylesheet.css"])

app.layout = html.Div([
        sidebar.sidebar,
        html.Div(content, id="page-content", style=CONTENT_STYLE)
    ])
    
if __name__ == "__main__":
    app.run_server(debug=True)