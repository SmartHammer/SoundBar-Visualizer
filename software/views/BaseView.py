# This Python file uses the following encoding: utf-8
from PySide2 import QtQuick


class BaseView(QtQuick.QQuickItem):
    def __init__(self, parent=None):
        super().__init__(parent)
