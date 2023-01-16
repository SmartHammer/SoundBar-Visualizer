# This Python file uses the following encoding: utf-8
from _3rdparty.libsoundtouch import SoundTouchSearcher
from PySide2.QtCore import QObject, Signal
from helper.singletondecorator import singleton
from threading import Thread, currentThread
import atexit


@singleton
class SoundTouchDeviceSearcher(QObject):
    finished = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._worker = None
        self._devices = []

    def startSearch(self, timeout=5):
        if not self._worker:
            self._timeout = timeout
            self._worker = Thread(target=self._search)
            self._worker.daemon = True
            self._worker.start()

    def getDevices(self):
        return self._devices

    def _search(self):
        @atexit.register
        def killed():
            print ("'CLEANLY' kill SoundTouchDeviceSearcher-thread: \
                [THREAD: %s]" % (currentThread().ident))
        self._devices = SoundTouchSearcher.searchSoundTouchDevices(self._timeout)
        self.finished.emit(self._devices)
        atexit.unregister(killed)
