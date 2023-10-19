from dash import html

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa"
}

sidebar = html.Div(
    [
        html.H2("Sidebar",className="display-4"),
        html.P("Sidebar layout for project", className="lead"),
    ],
    style=SIDEBAR_STYLE
)
