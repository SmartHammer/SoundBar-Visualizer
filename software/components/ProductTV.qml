import QtQuick 2.15
import QtGraphicalEffects 1.15
import VM 1.0

Item {
    id: productTV
    objectName: "productTV"
    anchors.fill: parent
    property SoundTouch context: null

    Image {
        id: image
        objectName: "image"
        anchors.fill: parent
        source: "../assets/tv.jpg"
    }

    Headline {
        id: headline
        objectName: "headline"
        anchors.top: productTV.top
        width: productTV.width
        height: 88
        iconHeight: height
        image: "../assets/tv-icon.png"
        name: "TV"
        clock: context ? Qt.formatTime(context.clock, "hh:mm") : ""
    }
}
