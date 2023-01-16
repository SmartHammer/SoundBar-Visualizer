# This Python file uses the following encoding: utf-8

from PySide2.QtCore import Property, Signal, Slot
from .BaseVM import BaseVM
from fsm.States import States
from controller.ViewManagerBase import ViewManagerBase
from models.SoundTouchSearchBackend import SoundTouchSearchBackend


class SoundTouchSearchVM(BaseVM):
    searchRunningChanged = Signal()

    def __init__(self, viewManager: ViewManagerBase, parent=None):
        super().__init__(viewManager, parent)
        self._searchTimeoutSec = 5
        self._searchRunning = True
        self._backend = SoundTouchSearchBackend(timeout=self._searchTimeoutSec,
                                                parent=self)
        self._backend.devicesChanged.connect(self._onDevicesChanged)

    @Slot(object)
    def _onDevicesChanged(self, devices):
        self._devices = devices
        self._searchRunning = False
        self.searchRunningChanged.emit()
        self._viewManager.switchState(States.Options.SoundTouch)

    def _getSearchRunning(self):
        return self._searchRunning

    searchRunning = Property(type=bool, fget=_getSearchRunning,
                             notify=searchRunningChanged)
