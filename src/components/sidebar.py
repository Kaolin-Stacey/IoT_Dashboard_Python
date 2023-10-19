from dash import html, Input, Output
import dash_daq as daq
from config import app
from datetime import datetime

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
        daq.LEDDisplay(
            id='digital_clock_led',
            value="",
            color="black",
            backgroundColor="transparent"
        ),
        html.P("Sidebar layout for project", className="lead"),
    ],
    style=SIDEBAR_STYLE
)
@app.callback(
    Output('digital_clock_led','value'),
    Input('interval-component','n_intervals')
)
def update_time(n_intervals):
    return datetime.now().strftime("%H:%M")
