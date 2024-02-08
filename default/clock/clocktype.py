from abc import ABC, abstractmethod


class ClockTypeInterface(ABC):
    @abstractmethod
    def content(self):
        pass
