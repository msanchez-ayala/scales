import QtQuick 2.15
import QtQuick.Controls 2.15


Page {
    id: root
    width: 500
    height: 475
    visible: true

    Rectangle {
        id: background
        anchors.fill: parent
        color: "white"
    }

    Rectangle {
        id: topBar
        height: 55
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        color: '#2699fb'

        Text {
            id: headerText
            text: 'Major scales'
            anchors.left: parent.left
            anchors.leftMargin: 10
            anchors.verticalCenter: parent.verticalCenter
            color: 'white'
            font.pointSize: 20
            font.bold: true
        }
    }

    Item {
        id: selectorsContainer
        width: rootNoteSelector.width
        height: rootNoteSelector.height + keySignatureSelector.height + 15
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: topBar.bottom
        anchors.topMargin: 30

        Selector {
            id: rootNoteSelector
            headerText: 'Root note'
            descText: 'The first note in the scale'
            comboModel: manager.rootNotes
            comboTextRole: 'noteName'
            onComboChanged: {
                keySignatureSelector.comboCurrentIndex = manager.onRootIndexChanged(comboCurrentIndex)
            }
            anchors.top: parent.top
            anchors.left: parent.left
        }

        Selector {
            id: keySignatureSelector
            headerText: 'Key signature'
            descText: 'The number of sharps or flats'
            comboModel: manager.keySignatures
            comboTextRole: 'signatureName'
            onComboChanged: {
                rootNoteSelector.comboCurrentIndex = manager.onKeySignatureIndexChanged(comboCurrentIndex)
            }
            anchors.top: rootNoteSelector.bottom
            anchors.topMargin: 15
            anchors.left: parent.left
        }
    }

    Text {
        id: noteCirclesHeader
        anchors.left: noteCircles.left
        anchors.top: selectorsContainer.bottom
        anchors.topMargin: 20
        font.pointSize: 20
        font.bold: true
        color: '#2699fb'
        text: 'Scale'
    }

    Row {
        id: noteCircles
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: noteCirclesHeader.bottom
        anchors.margins: 20
        spacing: 6
        Repeater {
            model: manager.scaleNoteNames
            delegate:
                NoteRect { text: display; degree: index + 1 }
        }
    }

    Rectangle {
        id: bottomBar
        height: 15
        color: '#f2f2f2'
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right

        Text {
            text: 'sanchezayala.marco@gmail.com'
            font.pointSize: 8
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: 5
        }
    }
}
