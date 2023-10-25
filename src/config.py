# global variables

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./assets/styles/style.css"])

ledOn = False
fanOn = False

temperatureVal = 26
temperatureThreshold = 25

humidityVal = 46





# email
host_email = "k29263306@gmail.com"
password = "bumsqpvbnmnmuljr"

recipient_email = "kaolin.stacey@gmail.com"

waitingOnReply = False
searchDate = None