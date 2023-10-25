from dash import html, Input, Output
import dash_daq as daq

from config import app
import config

# images taken from icons8.com
# https://icons8.com/icon/zT353tmi9iVj/ceiling-fan-off
# https://icons8.com/icon/mRZhnASfHcGB/ceiling-fan-off

component = html.Div(
    [
        html.Img(
            id="fan_image",
        ),
        daq.PowerButton(
            id="fanPowerButton",
            color="#FF6B6B",
            size=80
        )
    ],
    className="stateDiv"
)
@app.callback(
    Output('fanPowerButton','on'),
    Output('alert-auto','is_open'),
    Input('interval-component','n_intervals')
)
def updatePowerButton(n_intervals):
    return config.fanOn, config.waitingOnReply

@app.callback(
    Output('fan_image','src'),
    Input('fanPowerButton','on')
)
def isLedOn(on):
    config.fanOn = on
    return f'./assets/images/fan-{"on" if config.fanOn else "off"}.png'