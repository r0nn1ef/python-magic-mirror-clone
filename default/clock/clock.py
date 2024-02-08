from default.pod import PodInterface
from default.clock.digital import DigitalClock


class Clock(PodInterface):

    def __init__(self, config):
        clock_type = config["type"]
        if config["type"] == "digital":
            self.clock = DigitalClock(config)
        else:
            self.clock = None

    def content(self):
        return self.clock.content()
