"""
An simple Abstract Base Class for a realized distribution. Just makes sure that
all realizations have some required common methods and properties 💗 Absolutely
none of the type annotations work given that this is an Abstract Class. Just
here for future exploration.
"""

from abc import ABC, abstractmethod, abstractproperty
from typing import List, Tuple, Union, NoReturn


class BaseRealization(ABC):
    @abstractproperty
    def type(self) -> str:
        pass

    @abstractproperty
    def params(self) -> str:
        pass

    @abstractproperty
    def name(self) -> str:
        pass

    @abstractmethod
    def realization(self) -> Union[float, List[float], Tuple[float, float]]:
        pass

    @abstractmethod
    def check(self) -> Union[ValueError, NoReturn]:
        pass
