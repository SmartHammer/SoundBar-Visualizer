import QtQuick 2.15
import QtGraphicalEffects 1.15
import "../components"

Item {
    id: root
    objectName: "songViewer"

    property var track: ""
    property var extension: ""
    property var artist: ""
    property var album: ""
    property var image: ""

    Item {
        id: background
        anchors.fill: parent

        Image {
            id: backgroundImage
            objectName: "backgroundImage"
            anchors.fill: parent
            fillMode: Image.PreserveAspectCrop
            source: image ? image : ""
            smooth: true
        }

        FastBlur {
            id: blur
            anchors.fill: parent
            source: backgroundImage
            radius: 46
        }

        Rectangle {
            id: darkener
            objectName: "darkener"
            anchors.fill: backgroundImage
            color: "ghostwhite"
            opacity: 0.4
        }
    }

    Image {
        id: trackImage
        objectName: "trackImage"
        anchors.right: root.right
        anchors.bottom: root.bottom
        anchors.margins: {
            right: 20
            bottom: 20
        }
        height: 300
        fillMode: Image.PreserveAspectFit
        source: image ? image : ""

        layer.enabled: true
        layer.effect: DropShadow {
            anchors.fill: trackImage
            horizontalOffset: 8
            verticalOffset: 8
            radius: 8.0
            samples: 17
            color: "#80000000"
        }
    }

    TextWithShadow {
        id: trackName
        objectName: "trackName"
        anchors.left: root.left
        anchors.top: trackImage.top
        anchors.right: trackImage.left
        anchors.margins: {
            left: 20
            top: 0
            right: 20
            bottom: 20
        }
        color: "black"
        shadowColor: "white"
        font.pixelSize: 52
        font.bold: true
        wrapMode: Text.WordWrap
        horizontalAlignment: Text.AlignLeft
        text: track
    }

    TextWithShadow {
        id: artistName
        objectName: "artistName"
        anchors.left: root.left
        anchors.top: trackName.bottom
        anchors.right: trackImage.left
        anchors.margins: {
            left: 20
            top: 20
            right: 20
            bottom: 20
        }
        color: "black"
        shadowColor: "white"
        font.pixelSize: 48
        font.bold: true
        wrapMode: Text.WordWrap
        text: artist
    }

    TextWithShadow {
        id: albumTitle
        objectName: "albumTitle"
        anchors.left: root.left
        anchors.top: artistName.bottom
        anchors.right: trackImage.left
        anchors.margins: {
            left: 20
            top: 20
            right: 20
            bottom: 20
        }
        color: "black"
        shadowColor: "white"
        font.pixelSize: 42
        wrapMode: Text.WordWrap
        text: album
    }
}
