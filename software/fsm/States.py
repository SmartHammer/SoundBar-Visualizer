# This Python file uses the following encoding: utf-8

from PySide2 import QtCore
from enum import Enum


class States(QtCore.QObject):
    @QtCore.QEnum
    class Options(Enum):
        Undefined, StartUp, SoundTouch, Shazam = range(4)

    def getInitialState():
        return States.Options.StartUp
