import QtQuick 2.15

Item {
    id: componentPropertyViewer
    objectName: "componentPropertyViewer"

    Text {
        id: text
        objectName: "text"
        anchors.fill: parent
        text: "width:  " + parent.parent.width + "\n" +
              "height: " + parent.parent.height + "\n" +
              "x:      " + parent.parent.x + "\n" +
              "y:      " + parent.parent.y
    }
}
