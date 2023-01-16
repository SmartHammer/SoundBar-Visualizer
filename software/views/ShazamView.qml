import QtQuick 2.15
import QtQuick.Window 2.15
import Views 1.0
import States 1.0

BaseView {
    id: root
    objectName: "shazamView"
    width: Screen.width
    height: Screen.height
    x: 0
    y: 0
    focus: true
    property var context: null

    Rectangle {
        id: background
        objectName: "background"
        anchors.fill: parent

        Loader {
            id: loader
            objectName: "loader"
        }

        Binding {
            target: loader.item
            property: "context"
            value: root.context
        }

        Binding {
            target: loader.item
            property: "parent"
            value: background
        }
    }

    states: [
        State {
            name: "idle"
            PropertyChanges {
                target: background
                color: "#00b3ff"
            }
            when: context && (context.state.value === ShazamState.IDLE)
        },
        State {
            name: "listening"
            PropertyChanges {
                target: background
                color: "#00b3ff"
            }
            PropertyChanges {
                target: loader
                source: "../components/ShazamSearching.qml"
            }
            when: context && (context.state.value === ShazamState.LISTENING)
        },
        State {
            name: "searching"
            PropertyChanges {
                target: background
                color: "#00b3ff"
            }
            PropertyChanges {
                target: loader
                source: "../components/ShazamSearching.qml"
            }
            when: context && (context.state.value === ShazamState.SEARCHING)
        },
        State {
            name: "found"
            PropertyChanges {
                target: background
                color: "black"
            }
            PropertyChanges {
                target: loader
                source: "../components/ShazamResult.qml"
            }
            when: context && (context.state.value === ShazamState.FOUND)
        },
        State {
            name: "error"
            PropertyChanges {
                target: background
                color: "black"
            }
            PropertyChanges {
                target: loader
                source: "../components/ShazamResult.qml"
            }
            when: context && (context.state.value === ShazamState.ERROR)
        }
    ]

    // required for long press detection
    MouseArea {
        id: mouseArea
        objectName: "mouseArea"
        anchors.fill: parent

        onPressed: {
            if (context) {
                context.onMousePressed()
            }
        }

        onReleased: {
            if (context) {
                context.onMouseReleased()
            }
        }
    }
}
