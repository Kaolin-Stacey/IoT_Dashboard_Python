import RPi.GPIO as GPIO

# global variables

import dash
import dash_bootstrap_components as dbc
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "./assets/styles/style.css"])

ledOn = False
ledPin = 20

lightVal = 700

fanOn = False
fanEnablePin = 17
fanInput1Pin = 4
fanInput2Pin = 27

temperatureVal = 22

humidityVal = 35




# email
host_email = "k29263306@gmail.com"
password = "bumsqpvbnmnmuljr"

recipient_email = "kaolin.stacey@gmail.com"

waitingOnReply = False
searchDate = None

# user
current_user = None
temperatureThreshold = 25
lightThreshold = 400
humidityThreshold = 50

# bluetooth
nearby_devices = None