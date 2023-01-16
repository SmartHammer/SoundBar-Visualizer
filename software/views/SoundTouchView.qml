import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import Views 1.0
import States 1.0
import VM 1.0

BaseView {
    id: root
    objectName: "soundTouchView"
    width: Screen.width
    height: Screen.height
    x: 0
    y: 0
    focus: true
    property SoundTouch context: null

    Rectangle {
        id: background
        objectName: "background"
        anchors.fill: parent
        color: "black"

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
            name: "tv"
            PropertyChanges {
                target: loader
                source: "../components/ProductTV.qml"
            }
            when: context && (context.state.value === SoundtouchState.TV)
        },
        State {
            name: "webradio"
            PropertyChanges {
                target: loader
                source: "../components/WebRadio.qml"
            }
            when: context && (context.state.value === SoundtouchState.RADIO)
        },
        State {
            name: "mediaplayer"
            PropertyChanges {
                target: loader
                source: "../components/MediaPlayer.qml"
            }
            when: context && (context.state.value === SoundtouchState.MEDIA)
        },
        State {
            name: "standby"
            PropertyChanges {
                target: loader
                source: "../components/Standby.qml"
            }
            when: context && (context.state.value === SoundtouchState.STANDBY)
        }
    ]

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
