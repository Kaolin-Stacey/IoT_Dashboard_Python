from dash import html
import dash_bootstrap_components as dbc

import components.temperature
import components.humidity

content = [
    html.H1("IoT Project"),
    html.P("This is our IoT project"),
    components.temperature.component,
    components.humidity.component
]