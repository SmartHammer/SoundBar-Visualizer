# This Python file uses the following encoding: utf-8

from PySide2.QtQml import qmlRegisterType
from viewmodels.MainWindowVM import MainWindowVM
from viewmodels.SoundTouchSearchVM import SoundTouchSearchVM
from viewmodels.SoundTouchVM import SoundTouchVM
from viewmodels.ShazamVM import ShazamVM
from .States import States


qmlRegisterType(MainWindowVM, 'VM', 1, 0, 'MainWindow')
qmlRegisterType(ShazamVM, 'VM', 1, 0, 'Shazam')
qmlRegisterType(SoundTouchSearchVM, 'VM', 1, 0, 'SoundTouchSearch')
qmlRegisterType(SoundTouchVM, 'VM', 1, 0, 'SoundTouch')


class ViewContext:
    def __init__(self, parent=None):
        self._mainEntry: dict = {
            "qml": "views/MainWindow.qml",
            "contextName": "context",
            "vm": lambda parent: MainWindowVM(parent)
        }
        self._stateViewMap: dict = {
            States.Options.StartUp: {"qml": "views/SoundTouchSearchView.qml",
                                     "contextName": "context",
                                     "vm": lambda vm: SoundTouchSearchVM(vm)},
            States.Options.SoundTouch: {"qml": "views/SoundTouchView.qml",
                                        "contextName": "context",
                                        "vm": lambda vm: SoundTouchVM(vm)},
            States.Options.Shazam: {"qml": "views/ShazamView.qml",
                                    "contextName": "context",
                                    "vm": lambda vm: ShazamVM(vm)}}

    def getMainContent(self):
        return self._mainEntry

    def getStateContent(self, state: States.Options):
        return self._stateViewMap.get(state)
