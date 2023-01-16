# This Python file uses the following encoding: utf-8

from PySide2 import QtCore


class MainWindowVM(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    # -------------------------------------
    # Getter
    # -------------------------------------
    def _getAngle(self):
        return 0.0

    # -------------------------------------
    # Property
    # -------------------------------------
    angle = QtCore.Property(type=float, fget=_getAngle, constant=True)
