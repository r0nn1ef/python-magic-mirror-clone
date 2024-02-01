from os.path import exists
from dash import Dash, html, dcc, callback, Output, Input
import yaml

config = None

if exists("./config.yml"):
    with open("config.yml", 'r') as file:
        try:
            config = yaml.safe_load(file)
        except FileNotFoundError:
            print("Could not find config.yml file. Please copy config.default.yml in the root of your installation.")

if config is not None:
    PORT = int(config["app"]["port"])
    DEBUG = (config["app"]["debug"])
    TIME_FORMAT = config["app"]["time_format"]
    UNITS = config["app"]["units"]

    app = Dash(__name__)


    app.layout = html.Div(id="main-wrapper", children=[
        html.Div(id="region-fullscreen-below", className="region fullscreen below", children=[html.Div(id="region-full-screen-below-container", className="container", children=[])]),
        html.Div(id="region-top-bar", className="region top bar", children=[
            html.Div(id="region-top-bar-container", className="container"),
            html.Div(id="region-top-left", className="region top left", children=[html.Div(id="region-top-left-container", className="container", children=[])]),
            html.Div(id="region-top-center", className="region top center", children=[html.Div(id="region-top-center-container", className="container", children=[])]),
            html.Div(id="region-top-right", className="region top right", children=[html.Div(id="region-top-right-container", className="container", children=[])]),
        ]),
        html.Div(id="region-upper-third", className="region upper third", children=[html.Div(id="region-upper-third-container", className="container", children=[])]),
        html.Div(id="region-middle-center", className="region middle center", children=[html.Div(id="region-middle-center-container", className="container", children=[])]),
        html.Div(id="region-lower-third", className="region lower third", children=[html.Div(id="region-lower-third-content", className="container", children=[html.Br()])]),
        html.Div(id="region-bottom-bar", className="region bottom bar", children=[
            html.Div(id="region-bottom-bar-container", className="container"),
            html.Div(id="region-bottom-left", className="region bottom left", children=[html.Div(id="region-bottom-left-container", className="container", children=[])]),
            html.Div(id="region-bottom-center", className="region bottom center", children=[html.Div(id="region-bottom-center-container", className="container", children=[])]),
            html.Div(id="region-bottom-right", className="region bottom right", children=[html.Div(id="region-bottom-right-container", className="container", children=[])]),
        ]),
        html.Div(id="region-fullscreen-above", className="region fullscreen above", children=[html.Div(id="region-fullscreen-above-container", className="container", children=[])]),
    ])

    if __name__ == '__main__':
        app.run(port=PORT, debug=DEBUG)
else:
    print("Could not find config.yml file. Please copy config.default.yml in the root of your installation.")