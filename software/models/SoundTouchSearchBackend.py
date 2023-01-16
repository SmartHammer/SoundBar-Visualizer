# This Python file uses the following encoding: utf-8

from PySide2.QtCore import QObject, Slot, Signal
from .SoundTouchDeviceSearcher import SoundTouchDeviceSearcher


class SoundTouchSearchBackend(QObject):
    devicesChanged = Signal(object)

    def __init__(self, timeout=5, parent=None):
        super().__init__(parent)
        self._searcher = SoundTouchDeviceSearcher()
        self._searcher.finished.connect(self._onSearchFinished)
        self._searcher.startSearch(timeout)

    @Slot(object)
    def _onSearchFinished(self, devices):
        self._devices = devices
        self.devicesChanged.emit(devices)

    def getDevices(self):
        return self._searcher.getDevices()
