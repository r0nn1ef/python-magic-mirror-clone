from pod import PodInterface
from dash import html


class Weather(PodInterface):
    def __init__(self, config):
        self.config = config

    def content(self):
        return html.Div(children="Weather", className="", id="weather-wrapper")
