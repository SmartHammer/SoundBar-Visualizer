import QtQuick 2.15

Item {
    id: standby
    objectName: "standby"
    anchors.fill: parent

    property var context: null

    Image {
        id: image
        objectName: "image"
        anchors.fill: parent

        source: "../assets/i-feel-empty.jpg"
    }
}
