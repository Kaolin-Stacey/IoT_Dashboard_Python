# global variables

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./styles/styles.css"])

ledOn = False
temperatureVal = 0
humidityVal = 0

fanOn = False