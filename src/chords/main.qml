import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Item {
        id: root_text_item
        anchors.left: parent.left
        width: 45
        height: 40
        Text {
            id: root_text
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            text: 'Root:';
            font.pointSize: 16
        }
    }


    ComboBox {
        id: root_combo
        width: 70
        anchors.left: root_text_item.right
        model : ListModel {
        ListElement { text: "C" }
        ListElement { text: "D" }
        ListElement { text: "E"}
        ListElement { text: 'F'}
        }
    }

    Item {
        id: quality_text_item
        anchors.left: root_combo.right
        width: 45
        height: 40
        Text {
            id: quality_text
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            text: 'Quality:';
            font.pointSize: 16
        }
    }

    ComboBox {
        id: quality_combo
        width: 70
        anchors.left: quality_text_item.right
        model : ListModel {
        ListElement { text: "Major" }
        ListElement { text: "Minor" }
        ListElement { text: "Diminished"}
        ListElement { text: "Major 7" }
        ListElement { text: 'Dominant 7' }
        ListElement { text: "Minor 7" }
        ListElement { text: "Diminished 7" }
        }
    }

}
