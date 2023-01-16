# This Python file uses the following encoding: utf-8

from os import path
from PySide2.QtCore import QTimer, QObject, Property, Slot, Signal
from .BaseVM import BaseVM
from fsm.States import States
from controller.ViewManagerBase import ViewManagerBase
from models.ShazamBackend import ShazamBackend
from models.ShazamSearchState import ShazamSearchState
from .Header import Header
from .Song import Song
from .States import ShazamState


class ShazamVM(BaseVM):
    def __init__(self, viewManager: ViewManagerBase, parent=None):
        super().__init__(viewManager, parent)
        self._header: Header = Header("Shazam!", self._getShazamImage())
        self._song: Song = None
        self._state: ShazamState = None
        self._backend = ShazamBackend(self)
        self._backend.stateChanged.connect(self._onStateChanged)
        self._onStateChanged(self._backend.getState())
        self._backend.startSearch()

    stateChanged = Signal(ShazamState)

    @Slot()
    def _onStateChanged(self, state: ShazamSearchState):
        _state = ShazamState(ShazamState.Options.IDLE)
        if state == ShazamSearchState.LISTENING:
            _state = ShazamState(ShazamState.Options.LISTENING)
        elif state == ShazamSearchState.SEARCHING:
            _state = ShazamState(ShazamState.Options.SEARCHING)
        elif state == ShazamSearchState.FOUND:
            _song = Song(self._backend.getTrack(), self._backend.getArtist(), "", self._backend.getImage())
            if _song != self._song:
                self._song = _song
                _state = ShazamState(ShazamState.Options.FOUND)
            QTimer().singleShot(7000, self.fallbackToSoundTouchView)
        elif state == ShazamSearchState.ERROR:
            _state = ShazamState(ShazamState.Options.ERROR)
            QTimer().singleShot(7000, self.fallbackToSoundTouchView)
        if _state != self._state:
            self._state = _state
            self.stateChanged.emit(self._state)

    def fallbackToSoundTouchView(self):
        self._viewManager.switchState(States.Options.SoundTouch)

    def _getShazamImage(self):
        return path.join(self._viewManager.getRootPath(), "assets/shazam-blue.png")

    def _getSong(self):
        return self._song

    def _getHeader(self):
        return self._header

    def _getState(self):
        return self._state

    song = Property(type=QObject, fget=_getSong, constant=True)

    header = Property(type=QObject, fget=_getHeader, constant=True)

    state = Property(type=ShazamState, fget=_getState, notify=stateChanged)
