import QtQuick 2.15
import QtQuick.Window 2.15
import States 1.0

Item {
    id: root
    objectName: "shazamSearching"
    anchors.fill: parent
    property var context: null

    function getStateText() {
        var isListening = context
                && (context.state.value === ShazamState.LISTENING)
        var isSearching = context
                && (context.state.value === ShazamState.SEARCHING)
        return isListening ? "Listening..." : isSearching ? "Searching..." : "..."
    }

    Image {
        id: searchingImage
        objectName: "searchingImage"
        anchors.centerIn: parent
        property var context: root.context

        height: Screen.height / 2.0
        width: height
        source: "../assets/shazam-blue.png"

        SequentialAnimation {
            id: animation
            property int fullDuration: 3000
            loops: Animation.Infinite
            running: true
            NumberAnimation {
                target: searchingImage
                easing.period: 0.4
                easing.amplitude: 1.3
                easing.type: Easing.InElastic
                properties: "scale"
                duration: animation.fullDuration / 2
                from: 1.0
                to: 1.5
            }
            NumberAnimation {
                target: searchingImage
                easing.period: 0.4
                easing.amplitude: 1.3
                easing.type: Easing.OutElastic
                properties: "scale"
                duration: animation.fullDuration / 2
                from: 1.5
                to: 1.0
            }
        }
    }

    Text {
        id: searchingText
        objectName: "searchingText"
        color: "white"
        font.pixelSize: 32
        text: getStateText()

        anchors.horizontalCenter: root.horizontalCenter
        anchors.bottom: root.bottom
        anchors.margins: {
            bottom: 10
        }
    }
}
