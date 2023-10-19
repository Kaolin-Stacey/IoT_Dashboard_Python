import RPi.GPIO as GPIO

# global variables

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./assets/styles/style.css"])

ledOn = False
ledPin = 20

fanOn = False
fanEnablePin = 17
fanInput1Pin = 27
fanInput2Pin = 4


temperatureVal = 0
temperatureThreshold = 25

humidityVal = 0




# email
host_email = "k29263306@gmail.com"
password = "bumsqpvbnmnmuljr"

recipient_email = "kaolin.stacey@gmail.com"

waitingOnReply = False
searchDate = None