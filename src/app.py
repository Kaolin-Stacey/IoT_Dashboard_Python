from dash import html, dcc
from components import sidebar
from content import content
from config import app



CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem"
}

app.layout = html.Div([
        sidebar.sidebar,
        html.Div(content, id="page-content", className="content", style=CONTENT_STYLE),
        dcc.Interval(
            id='interval-component',
            interval=1000,
            n_intervals=0
        )
    ])
    
if __name__ == "__main__":
    import setupGPIO
    import threads
    try:
        print("running app")
        app.run_server(debug=True)
    except KeyboardInterrupt:
        import RPi.GPIO as GPIO
        GPIO.cleanup() 
