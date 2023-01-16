import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import Views 1.0
import "../components"

BaseView {
    id: soundTouchSearchView
    objectName: "soundTouchSearchView"
    width: Screen.width
    height: Screen.height
    x: 0
    y: 0
    focus: true
    property var context: null

    Rectangle {
        id: background
        objectName: "background"
        color: "black"
        anchors.fill: parent

        BusyIndicator {
            id: busyIndicator
            objectName: "busyIndicator"
            anchors.centerIn: parent
            height: Screen.height / 1.5
            width: height
            running: context ? context.searchRunning : false
            palette.dark: "orangered"
        }

        Text {
            id: statusText
            objectName: "statusText"
            color: "yellow"
            anchors.centerIn: parent
            text: "searching ..."
            font.pixelSize: 28
        }
    }
}
