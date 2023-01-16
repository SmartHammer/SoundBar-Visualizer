import QtQuick 2.15
import VM 1.0

Item {
    id: mediaPlayer
    objectName: "mediaPlayer"
    anchors.fill: parent

    property SoundTouch context: null

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
        anchors.top: mediaPlayer.top
        width: mediaPlayer.width
        height: 88
        image: context ? context.header.image : null
        name: context ? context.header.name : null
    }
}
