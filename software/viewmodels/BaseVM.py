# This Python file uses the following encoding: utf-8

from datetime import datetime
from PySide2.QtCore import QObject, Property, Signal, Slot, QTimer, QDateTime
from PySide2.QtGui import QGuiApplication
from controller.ViewManagerBase import ViewManagerBase
import logging


class BaseVM(QObject):
    def __init__(self, viewManager: ViewManagerBase, parent=None):
        super().__init__(parent)
        self._viewManager = viewManager
        self._pressTime = None
        self._longPressTimeSec = 2
        self._timer = QTimer()
        self._timer.timeout.connect(self._setClock)
        self._timer.start(30000)
        self._setClock()

    clockChanged = Signal()

    def onMousePressRelease(self):
        pass

    # -------------------------------------
    # Slots
    # -------------------------------------
    @Slot()
    def onMousePressed(self):
        logging.info("mouse pressed")
        self._pressTime = datetime.now()

    @Slot()
    def onMouseReleased(self):
        diff = (datetime.now() - self._pressTime).total_seconds()
        logging.info("mouse released after %i" % diff)
        if diff > self._longPressTimeSec:
            QGuiApplication.quit()
        else:
            self.onMousePressRelease()

    def _setClock(self):
        self.clockChanged.emit()

    def _getClock(self) -> QDateTime:
        return QDateTime.currentDateTime()

    clock = Property(type=QDateTime, fget=_getClock, notify=clockChanged)

    def activating(self):
        pass

    def activated(self):
        pass

    def deactivating(self):
        pass

    def deactivated(self):
        pass
