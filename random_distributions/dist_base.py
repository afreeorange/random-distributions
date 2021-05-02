"""
An simple Abstract Base Class for a realized distribution. Just makes sure that
all realizations have some required common methods.
"""

from abc import ABC, abstractmethod, abstractproperty


class BaseRealization(ABC):
    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def realization(self):
        pass

    @abstractmethod
    def check(self):
        pass
