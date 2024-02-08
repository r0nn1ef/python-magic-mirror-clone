from dash import html, dcc, Input, Output, callback
from datetime import datetime
import pytz

from default.clock.clocktype import ClockTypeInterface


class DigitalClock(ClockTypeInterface):

    def __init__(self, config):
        self.config = config

    def content(self):

        return html.Div(
            children=[
                html.Div(id="time-widget", className="date-time"),
                html.Div(id="date-widget", className="date-header"),
                dcc.Interval(
                    id="clock-interval",
                    interval=1 * 1000,
                    n_intervals=0
                )
            ],
            className="clock-widget",
        )

    @callback(
        [Output(component_id="date-widget", component_property="children")],
        [Input("clock-interval", "n_intervals")]
    )
    def update_date(self):
        df = "%H:%M:%S %p"
        return [html.Div(datetime.now().strftime(df), className="date-time")]

    @callback(
        [Output(component_id="time-widget", component_property="children")],
        [Input("clock-interval", "n_intervals")]
    )
    def update_time(self):
        # @todo Get date and time formats from instance configuration.
        tf = "%a, %b %d, %Y"
        return [html.Div(datetime.now().strftime(tf), className="date-header")]
