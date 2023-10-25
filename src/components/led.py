from dash import html, Input, Output
import dash_daq as daq

from config import app
import config

# images taken from icons8.com
# https://icons8.com/icon/zu4XG69PVx2m/light-off
# https://icons8.com/icon/e9V-XJYOmiTY/light-on

component = html.Div(
    [
        html.Img(
            id="light_image",
        ),
        daq.PowerButton(
            id="ledPowerButton",
            color="#FF6B6B",
            size=80
        )
    ],
    className="ledDiv"
)
@app.callback(
    Output('ledPowerButton','on'),
    Input('interval-component','n_intervals')
)
def updatePowerButton(n_intervals):
    return config.ledOn

@app.callback(
    Output('light_image','src'),
    Input('ledPowerButton','on')
)
def isLedOn(on):
    config.ledOn = on
    return f'./assets/images/light-{"on" if config.ledOn else "off"}.png'