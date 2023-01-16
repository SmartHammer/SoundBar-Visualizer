# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QObject, Property, Slot
import re


class Song(QObject):
    def __init__(self, title: str, artist: str, album: str, image: str, parent: QObject = None):
        super().__init__(parent)
        self._title = title
        self._artist = artist
        self._album = album
        self._image = image

    def _removeEverythingWithinBrackets(self, text: str) -> str:
        splitted: str = re.split(r'[\(|\[]', text)
        return "" if len(splitted) < 1 else splitted[0].rstrip()

    def _everythingWithinBrackets(self, text: str) -> str:
        splitted: str = re.split(r'[\(|\[]', text)
        return "" if len(splitted) < 1 else text[len(splitted[0]):]

    def _getTitle(self) -> str:
        return self._removeEverythingWithinBrackets(self._title)

    def _getTitleExtension(self) -> str:
        return self._everythingWithinBrackets(self._title)

    def _getArtist(self):
        return self._artist

    def _getAlbum(self):
        return self._album

    def _getImage(self):
        return self._image

    title = Property(type=str, fget=_getTitle, constant=True)

    titleExtension = Property(type=str, fget=_getTitleExtension, constant=True)

    artist = Property(type=str, fget=_getArtist, constant=True)

    album = Property(type=str, fget=_getAlbum, constant=True)

    image = Property(type=str, fget=_getImage, constant=True)

    @Slot(result=str)
    def getTitleFromTitleArtist(self) -> str:
        splitted = [] if self._artist is None else re.split(r' - ', self._artist)
        return "" if len(splitted) < 1 else self._removeEverythingWithinBrackets(splitted[0])

    @Slot(result=str)
    def getTitleExtensionFromTitleArtist(self) -> str:
        splitted = [] if self._artist is None else re.split(r' - ', self._artist)
        return "" if len(splitted) < 1 else self._everythingWithinBrackets(splitted[0])

    @Slot(result=str)
    def getArtistFromTitleArtist(self) -> str:
        splitted = [] if self._artist is None else re.split(r' - ', self._artist)
        return "" if len(splitted) < 2 else splitted[1]
