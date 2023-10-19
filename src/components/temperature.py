from dash import Input, Output
import dash_daq as daq

from config import app
import config

component = daq.Thermometer(
    id='temperature_display',
    value=0,
    min=10,
    max=30,
    showCurrentValue=True
)
@app.callback(
    Output('temperature_display','value'),
    Input('interval-component','n_intervals')
)
def updateTemperature(n_intervals):
    return config.temperatureVal