# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QEnum, QObject, Property
from enum import Enum, auto


class SoundtouchState(QObject):
    @QEnum
    class Options(Enum):
        STANDBY = auto()
        TV = auto()
        RADIO = auto()
        MEDIA = auto()

    def __init__(self, value: Options = None, parent: QObject = None):
        super().__init__(parent)
        self._value = value

    def _getValue(self):
        return self._value.value

    value = Property(int, fget = _getValue, constant = True)


class ShazamState(QObject):

    @QEnum
    class Options(Enum):
        IDLE = auto()
        LISTENING = auto()
        SEARCHING = auto()
        FOUND = auto()
        ERROR = auto()

    def __init__(self, value: Options = None, parent: QObject = None):
        super().__init__(parent)
        self._value = value

    def _getValue(self):
        return self._value.value

    value = Property(int, fget = _getValue, constant = True)
