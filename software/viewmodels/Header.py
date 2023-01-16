# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QObject, Property


class Header(QObject):
    def __init__(self, name: str, image: str, parent: QObject = None):
        super().__init__(parent)
        self._name: str = name
        self._image: str = image

    def _getName(self) -> str:
        return self._name

    def _getImage(self) -> str:
        return self._image

    name = Property(type=str, fget=_getName, constant=True)

    image = Property(type=str, fget=_getImage, constant=True)
