from dash import Input, Output
import dash_daq as daq

from config import app
import config

component = daq.Thermometer(
    id='temperature_display',
    value=0,
    min=10,
    max=30,
    showCurrentValue=True,
    label='Temperature',
    color="#FF6B6B"
)
@app.callback(
    Output('alert-auto','is_open'),
    Input('interval-component','n_intervals')
)
def sendEmail(n_intervals):
    if (config.temperatureVal > 24):
        print('Sending email')
        return True

@app.callback(
    Output('temperature_display','value'),
    Input('interval-component','n_intervals')
)
def updateTemperature(n_intervals):
    return config.temperatureVal