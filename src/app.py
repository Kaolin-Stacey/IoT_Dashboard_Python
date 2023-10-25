from dash import html, dcc
from components import sidebar
from content import content
from config import app
import threads

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem"
}

app.layout = html.Div([
        sidebar.sidebar,
        html.Div(content, id="page-content", className="content", style=CONTENT_STYLE),
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        )
    ])
    
if __name__ == "__main__":
    app.run_server(debug=True)