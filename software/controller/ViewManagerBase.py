# This Python file uses the following encoding: utf-8

from PySide2 import QtCore
from fsm.States import States


class ViewManagerBase(QtCore.QObject):
    def __init__(self, rootPath: str, parent=None):
        super().__init__(parent)
        self._rootPath=rootPath

    def switchState(self, state: States.Options):
        pass

    def getRootPath(self):
        return self._rootPath
