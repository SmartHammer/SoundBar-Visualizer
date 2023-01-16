# This Python file uses the following encoding: utf-8

from PySide2.QtCore import QObject, Signal
from threading import Thread, currentThread
from time import sleep
import atexit
from helper.MicrophoneListener import MicrophoneListener as MicListener
from .ShazamSearchState import ShazamSearchState
import asyncio
from shazamio import Shazam
from os import path, system
import logging
import traceback
from helper.MicrophoneListener import MicrophoneListener
from aiohttp.client_exceptions import ClientConnectorError


class ShazamBackend(QObject):
    stateChanged = Signal(ShazamSearchState)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._state = None
        self._beats = {1: None, 2: None, 3: None, 5: None, 7: None}
        self._worker: Thread = None
        self._mic = MicrophoneListener()
        self._setState(ShazamSearchState.IDLE)
        self._requiredDuration: int = 0
        if path.exists("/mnt/ramdisk"):
            self._path: str = "/mnt/ramdisk"
        else:
            self._path: str = path.dirname(path.abspath(__file__))
        self._mic = MicListener()
        self._shazam = Shazam()

    def _setState(self, state: ShazamSearchState):
        if not self._state or (state != self._state):
            self._state = state
            self.stateChanged.emit(self._state)

    def getRequiredDuration(self):
        return self._requiredDuration

    def getState(self):
        return self._state

    def getTrack(self):
        return self._track

    def getArtist(self):
        return self._artist

    def getImage(self):
        return self._image

    def startSearch(self):
        if self._worker and self._worker.is_alive():
            self._worker.join()
        self._worker = None
        self._worker = Thread(target=self._search)
        self._worker.daemon = True
        self._worker.start()

    def _search(self):
        try:
            @atexit.register
            def killed():
                print("'CLEANLY' kill 'Shazam' worker-thread: [THREAD: %s]" % (currentThread().ident))
            for duration in self._beats.keys():
                self._setState(ShazamSearchState.LISTENING)
                self._requiredDuration = duration
                if self._listen(duration):
                    self._setState(ShazamSearchState.SEARCHING)
                    self._findTrack()
                    if self._state == ShazamSearchState.FOUND:
                        break
        except ClientConnectorError as exc:
            errorText: str = repr(exc)
            logging.error(errorText + traceback.format_exc())
            system("reboot")
        except Exception as exc:
            errorText: str = repr(exc)
            logging.error(errorText + traceback.format_exc())
            self._setState(ShazamSearchState.ERROR)
        finally:
            atexit.unregister(killed)
            if self._state != ShazamSearchState.FOUND:
                self._setState(ShazamSearchState.ERROR)
            self.worker = None

    def _listen(self, duration: int) -> bool:
        _result: bool = True
        if path.exists("/mnt/ramdisk"):
            _result = self._mic.recordMonoToMp3(duration=duration, path=path.join(self._path, "shazam-this.mp3"))
        else:
            sleep(duration)
        return _result

    @staticmethod
    def _get_or_create_eventloop():
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return asyncio.get_event_loop()

    def _findTrack(self):

        async def _find():
            _shazamInfo: dict = await self._shazam.recognize_song(path.join(self._path, "shazam-this.mp3"))
            if "track" in _shazamInfo.keys():
                _track: dict = _shazamInfo["track"]
                if "title" in _track.keys():
                    self._track: str = _track["title"]
                if "subtitle" in _track.keys():
                    self._artist: str = _track["subtitle"]
                if "images" in _track.keys():
                    _images: dict = _track["images"]
                    if "coverarthq" in _images.keys():
                        self._image = _images["coverarthq"]
                self._setState(ShazamSearchState.FOUND)

        _loop = ShazamBackend._get_or_create_eventloop()
        _loop.run_until_complete(_find())
