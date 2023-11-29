from dash import html, Input, Output
import dash_daq as daq

from config import app
import config

component = daq.Gauge(
    id='lumens_display',
    value=800,
    min=0,
    max=1000,
    units="lumens",
    showCurrentValue=True,
    label='Lumens'
)

@app.callback(
    Output('lumens_display','value'),
    Input('interval-component','n_intervals')
)
def lumens(n_intervals):
    from config import lightVal
    return lightVal