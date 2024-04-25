# This Python file uses the following encoding: utf-8

from PySide2.QtCore import Property, QTimer, Signal, Slot
from .BaseVM import BaseVM
from fsm.States import States
from controller.ViewManagerBase import ViewManagerBase
from models.SoundTouchSearchBackend import SoundTouchSearchBackend


class SoundTouchSearchVM(BaseVM):
    searchRunningChanged = Signal()

    def __init__(self, viewManager: ViewManagerBase, parent=None):
        super().__init__(viewManager, parent)
        self._searchTimeoutSec = 5
        self._startSearching()
        self._timer = QTimer()

    def _startSearching(self):
        print("start searching")
        self._searchRunning = True
        self.searchRunningChanged.emit()
        self._backend = SoundTouchSearchBackend(timeout=self._searchTimeoutSec, parent=self)
        self._backend.devicesChanged.connect(self._onDevicesChanged)

    @Slot(object)
    def _onDevicesChanged(self, devices):
        self._devices = devices
        self._backend.devicesChanged.disconnect(self._onDevicesChanged)
        self._backend = None
        self._searchRunning = False
        self.searchRunningChanged.emit()
        print(devices)
        if devices is not None and len(devices) > 0:
            self._viewManager.switchState(States.Options.SoundTouch)
        else:
            self._timer.setSingleShot(True)
            self._timer.timeout.connect(self._startSearching)
            self._timer.start(self._searchTimeoutSec * 1000)


    def _getSearchRunning(self):
        return self._searchRunning

    searchRunning = Property(type=bool, fget=_getSearchRunning, notify=searchRunningChanged)
