from dash import html, Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq
from config import app
import config
from datetime import datetime

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "display": "flex",
    "flex-direction": "column",
    "align-items":"center"
}

sidebar = html.Div(
    [
        daq.LEDDisplay(
            id='digital_clock_led',
            className="timeLed",
            value="",
            color="white",
            backgroundColor="transparent"
        ),
        html.P("IoT Project", className="lead"),
        dbc.Alert(
            "An email has been sent out",
            id="alert-auto",
            is_open=False,
            duration=5000
        ),
        html.Span("",id="current_user"),
        html.Span("",id="temp_thres"),
        html.Span("",id="humid_thres"),
        html.Span("",id="light_thres"),
    ],
    className="sidebar",
    style=SIDEBAR_STYLE
)
@app.callback(
    Output('digital_clock_led','value'),
    Output('current_user','children'),
    Output('temp_thres','children'),
    Output('humid_thres','children'),
    Output('light_thres','children'),
    Input('interval-component','n_intervals')
)
def update_time(n_intervals):
    return datetime.now().strftime("%H:%M:%S"), config.current_user, config.temperatureThreshold, config.humidityThreshold, config.lightThreshold