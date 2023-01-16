# This Python file uses the following encoding: utf-8

from PySide2.QtCore import QObject, QTimer
from PySide2.QtCore import Property, Signal, Slot
from .BaseVM import BaseVM
from controller.ViewManagerBase import ViewManagerBase
from models.SoundTouchBackend import SoundTouchBackend
from models.ShazamBackend import ShazamBackend
from models.ShazamSearchState import ShazamSearchState
from viewmodels.Header import Header
from viewmodels.Song import Song
from viewmodels.States import SoundtouchState
import logging
from subprocess import run


class SoundTouchVM(BaseVM):
    def __init__(self, viewManager: ViewManagerBase, parent=None):
        super().__init__(viewManager, parent)
        logging.info("create SoundTouch view model")
        self._backend = SoundTouchBackend(parent=self)
        self._shazamBackend = ShazamBackend(parent=self)
        self._shazamBackend.stateChanged.connect(self._onShazamStateChanged)
        self._device = self._backend.getSelectedDevice()
        self._header: Header = None
        self._song: Song = None
        self._screenOffTimer: QTimer = None
        self._state: SoundtouchState = None
        self._displayIsOff: bool = True
        self._displayOn()
        if self._device:
            self._backend.statusChanged.connect(self._onStatusChanged)
            self._onStatusChanged(self._device.status())

    headerChanged = Signal(QObject)
    songChanged = Signal(QObject)
    stateChanged = Signal(SoundtouchState)

    @Slot(object)
    def _onStatusChanged(self, status: object):
        self._status = status
        self._setHeader()
        self._setSong()
        self._setState()

    @Slot()
    def _onShazamStateChanged(self, state: ShazamSearchState):
        if state == ShazamSearchState.FOUND:
            _artist: str = self._shazamBackend.getTrack() + " - " + self._shazamBackend.getArtist()
            _song = Song("", _artist, "", self._shazamBackend.getImage())
            if _song != self._song:
                self._song = _song
                self.songChanged.emit(self._song)
            _requiredDuration = self._shazamBackend.getRequiredDuration()
            QTimer.singleShot(7000 - _requiredDuration * 1000, self._setState)
        elif state == ShazamSearchState.ERROR:
            _requiredDuration = self._shazamBackend.getRequiredDuration()
            QTimer.singleShot(7000 - _requiredDuration * 1000, lambda: self._onStatusChanged(self._device.status()))

    def _getHeader(self):
        return self._header

    def _getSong(self):
        return self._song

    def _getState(self):
        return self._state

    header = Property(type=QObject, fget=_getHeader, notify=headerChanged)

    song = Property(type=QObject, fget=_getSong, notify=songChanged)

    state = Property(type=SoundtouchState, fget=_getState, notify=stateChanged)

    def _tryShazam(self):
        self._shazamBackend.startSearch()

    def _stopShazam(self):
        self._shazamBackend.stop()

    def _displayOn(self):
        if self._displayIsOff:
            run('vcgencmd display_power 1', shell=True)
            self._displayIsOff = False

    def _displayOff(self):
        if not self._displayIsOff:
            run('vcgencmd display_power 0', shell=True)
            self._displayIsOff = True

    def _startScreenOffTimer(self):
        if (self._screenOffTimer is not None) and self._screenOffTimer.isActive():
            self._screenOffTimer.stop()
        self._screenOffTimer = QTimer()
        self._screenOffTimer.setSingleShot(True)
        self._screenOffTimer.setInterval(10000)
        self._screenOffTimer.timeout.connect(self._displayOff)
        self._screenOffTimer.start()

    def _stopScreenOffTimer(self):
        if (self._screenOffTimer is not None) and self._screenOffTimer.isActive():
            self._screenOffTimer.stop()
        self._displayOn()

    def _setState(self):
        _state = SoundtouchState(SoundtouchState.Options.MEDIA)
        if self._isStandby():
            _state = SoundtouchState(SoundtouchState.Options.STANDBY)
            self._startScreenOffTimer()
        elif self._isTV():
            self._stopScreenOffTimer()
            _state = SoundtouchState(SoundtouchState.Options.TV)
        elif self._isRadio():
            self._stopScreenOffTimer()
            _state = SoundtouchState(SoundtouchState.Options.RADIO)
            if (self._status.artist is None) or (self._status.artist == ""):
                self._tryShazam()
            else:
                self._stopShazam()
        if _state != self._state:
            _old = self._state
            self._state = _state
            self.stateChanged.emit(self._state)
            if self._isStandby() and (_old is not None) and (_old._value is not SoundtouchState.Options.STANDBY):
                self._startScreenOffTimer()

    def _setHeader(self):
        _header = Header(self._getStationName(), self._getStationImage(), self)
        if _header != self._header:
            self._header = _header
            self.headerChanged.emit(self._header)

    def _setSong(self):
        _song = Song(self._getTrack(), self._getArtist(), self._getAlbum(), self._getImage(), self)
        if _song != self._song:
            self._song = _song
            self.songChanged.emit(self._song)

    def _isStandby(self):
        return self._status and (self._status.source == "STANDBY")

    def _isTV(self):
        return self._status and (self._status.source == "PRODUCT") and (self._status.content_item.source_account == "TV")

    def _isRadio(self):
        return self._status and (self._status.stream_type == "RADIO_STREAMING")

    def _getArtist(self):
        if self._status:
            return self._status.artist
        else:
            return ""

    def _getTrack(self):
        if self._status:
            return self._status.track
        else:
            return ""

    def _getAlbum(self):
        if self._status:
            return self._status.album
        else:
            return ""

    def _getStationName(self):
        if self._status:
            return self._status.content_item.name
        else:
            return ""

    def _getStationImage(self):
        if self._status:
            return self._status.content_item.image
        else:
            return ""

    def _getImage(self):
        if self._status:
            return self._status.image
        else:
            return ""

    def onMousePressRelease(self):
        if self._isStandby():
            run('vcgencmd display_power 1', shell=True)
            self._startScreenOffTimer()
