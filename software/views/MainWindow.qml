import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    id: mainWindow
    objectName: "mainWindow"
    visible: true
    visibility: Window.FullScreen
    //    flags: Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
    property var context: null

    Rectangle {
        id: frame
        objectName: "frame"
        anchors.fill: parent
        color: "black"

        rotation: {
            context ? context.angle : 0
        }

        Item {
            id: content
            objectName: "content"
            anchors.fill: parent
        }
    }
}
