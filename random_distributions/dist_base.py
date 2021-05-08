"""
An simple Abstract Base Class for a realized distribution. Just makes sure that
all realizations have some required common methods and properties 💗 

Still learning MyPy and haven't seen the type annotations show up in the
derived class 🤷‍♂️. Just here for future exploration.
"""

from abc import ABCMeta, abstractmethod
from typing import List, Tuple, Union, NoReturn


class BaseRealization(ABCMeta):
    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def params(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def realization(self) -> Union[float, List[float], Tuple[float, float]]:
        pass

    @abstractmethod
    def check(self) -> Union[ValueError, NoReturn]:
        pass
