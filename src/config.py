# global variables

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./assets/styles/style.css"])

ledOn = False
temperatureVal = 22
humidityVal = 46

fanOn = False


# email
sender_email = "k29263306@gmail.com"
recipient_email = ""

password = ""
email_host = "gmail.com"
email_port = "465"