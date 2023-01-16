import QtQuick 2.15
import QtGraphicalEffects 1.15

Item {
    id: root
    objectName: "headline"
    property string name: ""
    property string image: ""
    property string clock: ""
    property int iconHeight: 48

    Rectangle {
        id: background
        objectName: "background"
        anchors.fill: parent
        color: "#A0000000"
    }

    DropShadow {
        anchors.fill: background
        horizontalOffset: 8
        verticalOffset: 8
        radius: 8.0
        samples: 17
        color: "#80000000"
        source: background
    }

    Image {
        id: stationImage
        objectName: "stationImage"
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        height: iconHeight
        fillMode: Image.PreserveAspectFit
        anchors.margins: {
            left: 20
        }
        source: image
    }

    Text {
        id: stationName
        objectName: "stationName"
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: stationImage.right
        anchors.margins: {
            left: 20
        }
        verticalAlignment: Text.AlignVCenter
        color: "orange"
        font.pixelSize: 42
        text: name
    }

    Text {
        id: clockText
        objectName: "clockText"
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
        anchors.margins: {
            left: 20
            right: 20
        }
        verticalAlignment: Text.AlignVCenter
        color: "orange"
        font.pixelSize: 42
        text: clock
    }
}
