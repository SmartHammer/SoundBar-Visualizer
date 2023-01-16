import QtQuick 2.15

Item {
    id: root
    objectName: "shazamResult"
    anchors.fill: parent

    property var context: null

    SongViewer {
        id: songViewer
        objectName: "songViewer"
        anchors.fill: parent
        track: context ? context.song.title : null
        artist: context ? context.song.artist : null
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
