import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: root
    width: 450
    height: 100

    property alias headerText: headerText.text
    property alias descText: descText.text
    property alias comboModel: combo.model
    property alias comboTextRole: combo.textRole
    property alias comboCurrentIndex: combo.currentIndex

    signal comboChanged

    Rectangle {
        id: rectBorder
        anchors.fill: parent
        color: 'white'
        border.color: '#bce0fd'
        border.width: 1
    }

    Item {
        id: textItem
        height: headerText.height + descText.height + 4
        anchors.verticalCenter: root.verticalCenter
        anchors.left: root.left
        anchors.leftMargin: 20

        Text {
            id: headerText
            color: '#2699fb'
            font.pointSize: 20
            font.bold: true
        }

        Text {
            id: descText
            anchors.top: headerText.bottom
            anchors.topMargin: 4
            color: '#2699fb'
            font.pointSize: 14
        }
    }

    ComboBox {
        id: combo
        x: (3/5) * root.width
        width: 200
        height: 40
        anchors.verticalCenter: root.verticalCenter
        editable: false
        font.pixelSize: 20
        anchors.right: root.right
        anchors.rightMargin: 20

        onCurrentIndexChanged: { root.comboChanged() }
    }
}
