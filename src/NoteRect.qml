import QtQuick 2.15

Item {
    id: root
    property alias text: noteName.text
    property alias degree: scaleDegree.text

    width: 50
    height: 50

    Rectangle {
        id: rect
        anchors.fill: parent
        color: '#2699fb'
        radius: 5

        MouseArea {
            anchors.fill: parent
            enabled: true
            hoverEnabled: true
            onEntered: { rect.color = '#f5c26c' }
            onExited: { rect.color = '#2699fb' }
            onClicked: { console.log(noteName.text) }
        }
    }
    Text {
        id: scaleDegree
        anchors.top: parent.top
        anchors.topMargin: 3
        anchors.left: parent.left
        anchors.leftMargin: 5
        color: 'white'
        font.pointSize: 10
    }

    Text {
        id: noteName
        anchors.fill: parent
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        color: 'white'
        font.pointSize: 20
        font.bold: true
    }
}
/*##^##
Designer {
    D{i:0;formeditorZoom:1.659999966621399}
}
##^##*/
