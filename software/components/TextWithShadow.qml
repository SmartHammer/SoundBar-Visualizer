import QtQuick 2.15
import QtGraphicalEffects 1.15

Text {
    id: root
    property string shadowColor: "black"
    property int shadowRadius: 5
    property int shadowHorizontalOffset: 0
    property int shadowVerticalOffset: 0

    layer.enabled: true
    layer.effect: DropShadow {
        horizontalOffset: shadowHorizontalOffset
        verticalOffset: shadowVerticalOffset
        color: shadowColor
        radius: shadowRadius
        samples: shadowRadius * 2 + 1
    }
}
