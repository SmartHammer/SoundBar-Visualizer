# This Python file uses the following encoding: utf-8
from enum import Enum, auto


class ShazamSearchState(Enum):
    IDLE = auto()
    LISTENING = auto()
    SEARCHING = auto()
    FOUND = auto()
    ERROR = auto()
