from dash import Dash, html, dcc, Input, Output, callback
import dash_daq as daq
from datetime import datetime
from random import randrange
import pytz

from pod import PodInterface



class Clock(PodInterface):

    def __init__(self, config):
        self.config = config
        self.now = None
        self._get_time()

    def content(self):
        if hasattr(self.config, "id"):
            widget_id = self.config["id"]
        else:
            widget_id = "clock-widget-" + str(randrange(1, 1000, 1))

        cssclassname = []
        if self.config["background"] == "transparent" or self.config["background"] == "none":
            cssclassname.append("no-background")
        if "show_border" in self.config:
            if self.config["show_border"] == False:
                cssclassname.append("no-border")

        if "size" in self.config:
            font_size = self.config["size"]
        else:
            font_size = 32

        if "time_format" in self.config:
            tf = self.config["time_format"]
        else:
            tf = "%H:%M:%S"

        if "date_format" in self.config:
            df = self.config["date_format"]
        else:
            df = "%a, %b %d, %Y"
        # clock = daq.LEDDisplay(
        #     id=widget_id,
        #     value=now.strftime(tf),
        #     color=self.config["color"],
        #     backgroundColor=self.config["background"],
        #     className=" ".join(cssclassname),
        #     size=font_size
        # )

        return html.Div([
            html.Div(id="time-widget", className="date-time"),
            html.Div(id="date-widget", className="date-header"),
            dcc.Interval(
                id="clock-interval",
                interval=1 * 1000,
                n_intervals=0
            )
        ],
        className="clock-widget")

    @callback(
        [Output(component_id="date-widget", component_property="children")],
        [Input("clock-interval", "n_intervals")]
    )
    def update_date(self):
        # print(self.config["time_format"])
        tf = "%H:%M:%S %p"
        return [html.Div(datetime.now().strftime(tf), className="date-time")]

    @callback(
        [Output(component_id="time-widget", component_property="children")],
        [Input("clock-interval", "n_intervals")]
    )
    def update_time(self):
        # if "timezone" in self.config:
        #     now = datetime.now(pytz.timezone(self.config["timezone"]))
        # else:
        #     now = datetime.now()
        # if "time_format" in self.config:
        #     tf = self.config["time_format"]
        # else:
        #     tf = "%H:%M:%S"
        #
        # if "date_format" in self.config:
        #     df = self.config["date_format"]
        # else:
        #     df = "%a, %b %d, %Y"
        tf = "%H:%M:%S %p"
        df = "%a, %b %d, %Y"
        return [html.Div(datetime.now().strftime(df), className="date-header")]

    def _get_time(self):
        if "timezone" in self.config:
            self.now = datetime.now(pytz.timezone(self.config["timezone"]))
        else:
            self.now = datetime.now()
