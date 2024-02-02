import os
import yaml
from dash import Dash, html


class Mirror:
    def __init__(self, name, config_path):
        self._app = Dash(name)
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                try:
                    y = yaml.safe_load(file)
                    file.close()
                    self.config = y["app"]
                    self.modules = {}
                    for item in self.config["modules"]:
                        self.modules[item] = self.config["modules"][item]
                except FileNotFoundError:
                    self.config = None
        self._build_layout()

    def _build_layout(self):
        fullscreen_below_content = html.Div(children=[], className="container", id="region-fullscreen-below-container")
        top_bar_content = html.Div(children=[], className="container", id="region-top-bar-container")
        top_left_content = html.Div(children=[], className="container", id="region-top-left-container")
        top_center_content = html.Div(children=[], className="container", id="region-top-center-container")
        top_right_content = html.Div(children=[], className="container", id="region-top-right-container")
        upper_third_content = html.Div(children=[], className="container", id="region-upper-third-container")
        middle_center_content = html.Div(children=[], className="container", id="region-middle-center-container")
        lower_third_content = html.Div(children=[html.Br()], className="container", id="region-lower-third-content")
        bottom_bar_content = html.Div(children=[], className="container", id="region-bottom-bar-container")
        bottom_left_content = html.Div(children=[], className="container", id="region-bottom-left-container")
        bottom_center_content = html.Div(children=[], className="container", id="region-bottom-center-container")
        bottom_right_content = html.Div(children=[], className="container", id="region-bottom-right-container")
        fullscreen_above_content = html.Div(children=[], className="container", id="region-fullscreen-above-container")

        if hasattr(self, "config"):
            print(self.modules)
        else:
            # If no config is found, show an error message when the dashboard is run.
            middle_center_content.children.append("Missing configuration file. Please follow the instructions in the README.md file to create your configuration.")
        # Build the Dash app layout after populating the content containers above.
        self._app.layout = html.Div(id="main-wrapper", children=[
            html.Div(id="region-fullscreen-below", className="region fullscreen below", children=[
                fullscreen_below_content
            ]),
            html.Div(id="region-top-bar", className="region top bar", children=[
                top_bar_content,
                html.Div(id="region-top-left", className="region top left", children=[
                    top_left_content
                ]),
                html.Div(id="region-top-center", className="region top center", children=[
                    top_center_content
                ]),
                html.Div(id="region-top-right", className="region top right", children=[
                    top_right_content
                ]),
            ]),
            html.Div(id="region-upper-third", className="region upper third", children=[
                upper_third_content
            ]),
            html.Div(id="region-middle-center", className="region middle center", children=[
                middle_center_content
            ]),
            html.Div(id="region-lower-third", className="region lower third", children=[
                lower_third_content
            ]),
            html.Div(id="region-bottom-bar", className="region bottom bar", children=[
                bottom_bar_content,
                html.Div(id="region-bottom-left", className="region bottom left", children=[
                    bottom_left_content
                ]),
                html.Div(id="region-bottom-center", className="region bottom center", children=[
                    bottom_center_content
                ]),
                html.Div(id="region-bottom-right", className="region bottom right", children=[
                    bottom_right_content
                ]),
            ]),
            html.Div(id="region-fullscreen-above", className="region fullscreen above", children=[
                fullscreen_above_content
            ]),
        ])

    def run(self):
        if hasattr(self, "config"):
            PORT = self.config["port"]
            DEBUG = self.config["debug"]
        else:
            PORT = 8080
            DEBUG = True

        self._app.run(port=PORT, debug=DEBUG)
