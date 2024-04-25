# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QObject, Signal
from .SoundTouchDeviceSearcher import SoundTouchDeviceSearcher
from pickle import load, dump
from os import path
import logging


class SoundTouchBackend(QObject):
    statusChanged = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._searcher = SoundTouchDeviceSearcher()
        self._devices = self._searcher.getDevices()
        print(self._devices)
        self._path: str = path.dirname(path.abspath(__file__))
        if len(self._devices) == 0:
            _dump: str = path.join(self._path, "soundtouch.dump")
            if path.exists(_dump):
                with open(_dump, "rb") as f:
                    self._devices = load(f)
        self._selectedDevice = None
        self._getSelectedDeviceId()
        if self._selectedDevice:
            logging.info("add status listener")
            self._selectedDevice.add_status_listener(self._onStatusChanged)
            self._selectedDevice.start_notification()
            self._selectedDevice.refresh_status()
            self._onStatusChanged(self._selectedDevice.status())

    def _onStatusChanged(self, status: object):
        self.statusChanged.emit(status)

    def _getSelectedDeviceId(self):
        _selected: str = path.join(self._path, "selected.pickle")
        _deviceId = None
        if path.exists(_selected):
            with open(_selected, "rb") as f:
                try:
                    _deviceId = load(f)
                finally:
                    pass
        if _deviceId:
            self._selectedDevice = next(filter(lambda _device: _device.config.device_id == _deviceId, self._devices))
        if not self._selectedDevice and len(self._devices) != 0:
            self._selectedDevice = self._devices[0]
        if _deviceId != self._selectedDevice.config.device_id:
            with open(_selected, "wb") as f:
                dump(self._selectedDevice.config.device_id, f)

    def getDevices(self):
        return self._devices

    def getSelectedDevice(self):
        return self._selectedDevice
