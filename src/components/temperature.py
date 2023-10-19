from dash import Input, Output
import dash_daq as daq

from config import app

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
    Output('temperature_display','value'),
    Input('interval-component','n_intervals')
)
def updateTemperature(n_intervals):
    import config
    # print(config.temperatureVal)
    return config.temperatureVal