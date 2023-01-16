import QtQuick 2.15
import VM 1.0

Item {
    id: root
    objectName: "webRadio"
    anchors.fill: parent

    property SoundTouch context: null

    SongViewer {
        id: songViewer
        objectName: "songViewer"
        anchors.fill: parent
        track: context ? context.song.getTitleFromTitleArtist() : null
        artist: context ? context.song.getArtistFromTitleArtist() : null
        album: context ? context.song.album : null
        image: context ? context.song.image : null
    }

    Headline {
        id: headline
        objectName: "headline"
        anchors.top: root.top
        width: root.width
        height: 88
        image: context ? context.header.image : null
        name: context ? context.header.name : null
    }
}
