from dash import Input, Output
import dash_daq as daq

from config import app
import config

component = daq.Gauge(
    id='humidity_display',
    value=0,
    min=20,
    max=70,
    units="%",
    showCurrentValue=True,
    label='Humidity',
    color="#FF6B6B"
)
@app.callback(
    Output('humidity_display','value'),
    Input('interval-component','n_intervals')
)
def updateHumidity(n_intervals):
    return config.humidityVal