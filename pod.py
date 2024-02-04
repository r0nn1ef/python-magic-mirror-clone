from abc import ABC, abstractmethod


class PodInterface(ABC):
    @abstractmethod
    def content(self):
        pass
