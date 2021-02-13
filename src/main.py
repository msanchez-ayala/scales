import os
import sys
from typing import Iterable
from typing import Union

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtCore import QObject
from PySide2.QtCore import QUrl
from PySide2.QtCore import Slot
from PySide2.QtCore import Property
from PySide2.QtCore import QStringListModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QStandardItemModel
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtQuick import QQuickView
from PySide2.QtQuickWidgets import QQuickWidget

from backend import scales
from backend import notes
from backend.notes import Note


NOTE_ROLE = QtCore.Qt.UserRole + 1000
NOTE_NAME_ROLE = QtCore.Qt.UserRole + 1001
SIGNATUTE_NAME_ROLE = QtCore.Qt.UserRole + 1002

FLAT = 'Flat'
SHARP = 'Sharp'
NO_ACCIDENTALS = 'Flats/Sharps'


class RootNotes(QStandardItemModel):
    """
    A collection of note enums and note names.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        roles = {
            NOTE_ROLE: b'noteEnum',
            NOTE_NAME_ROLE: b'noteName'
        }
        self.setItemRoleNames(roles)

        root_notes = notes.USED_KEYS
        root_notes = sorted(root_notes, key=lambda root: root.value)
        self.addNotes(root_notes)

    def addNotes(self, notes: Iterable[Note]):
        """
        Add multiple rows of note data to the model.
        """
        for note in notes:
            self.addNote(note)

    def addNote(self, note: Note):
        """
        Add a row of note data to the model.
        """
        item = QtGui.QStandardItem()
        item.setData(note, NOTE_ROLE)
        item.setData(note.value, NOTE_NAME_ROLE)
        self.appendRow(item)


class KeySignatures(QStandardItemModel):
    """
    A collection of key root enums (Note) and their key signatures.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        roles = {
            NOTE_ROLE: b'rootNote',
            SIGNATUTE_NAME_ROLE: b'signatureName'
        }
        self.setItemRoleNames(roles)
        for root in notes.ROOT_ACCIDENTALS_MAP.keys():
            self.addSignature(root)

    def addSignature(self, root: Note):
        """
        Add a row of key signature data based on a root note.
        """
        signature_name = self._generateSignatureName(root)
        item = QtGui.QStandardItem()
        item.setData(root, NOTE_ROLE)
        item.setData(signature_name, SIGNATUTE_NAME_ROLE)
        self.appendRow(item)

    def _generateSignatureName(self, root: Note) -> str:
        """
        Generate the key signature name from a root note.
        E.g: _generateSignatureName(Note.E) -> '4 Sharps'.
        """
        accidental = NO_ACCIDENTALS
        if root in notes.FLAT_KEYS:
            accidental = FLAT
        elif root in notes.SHARP_KEYS:
            accidental = SHARP
        num_accidentals = notes.ROOT_ACCIDENTALS_MAP[root]
        if num_accidentals > 1:
            accidental += 's'
        return f'{num_accidentals} {accidental}'


class Manager(QObject):
    """
    Manages models for QML views and contains logic for some event handling
    with decorated methods.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._root_notes = RootNotes()
        self._scale_note_names = QStringListModel()
        # Initializing this model last sets the starting key to C because of
        # ROOTS_ACCIDENTAL_MAP
        self._key_signatures = KeySignatures()

    @Property(QtCore.QObject)
    def rootNotes(self):
        return self._root_notes

    @Property(QtCore.QObject)
    def scaleNoteNames(self):
        return self._scale_note_names

    @Property(QtCore.QObject)
    def keySignatures(self):
        return self._key_signatures

    @Slot(int, result=int)
    def onRootIndexChanged(self, combo_index: int):
        """
        Determine the currently selected root note to update the scale note
        names. Returns the index that the key signatures combo should be set to.
        """
        item = self._root_notes.item(combo_index)
        new_root = item.data(NOTE_ROLE)
        self._updateScaleNoteNames(new_root)
        return self._getComboIndex(self._key_signatures, new_root)

    @Slot(int, result=int)
    def onKeySignatureIndexChanged(self, combo_index):
        """
        Determine the root note of the currently selected key signature to
        update the scale note names. Returns the index that the root combo
        should be set to.
        """
        item = self._key_signatures.item(combo_index)
        new_root = item.data(NOTE_ROLE)
        self._updateScaleNoteNames(new_root)
        return self._getComboIndex(self._root_notes, new_root)

    def _getComboIndex(self,
                       model: Union[RootNotes, KeySignatures],
                       root: Note) -> int:
        """
        Return the combo index to set `model`'s view to. This is th same as the
        row number within `model` where `root` is stored.
        """
        for row in range(model.rowCount()):
            item = model.item(row)
            if item.data(NOTE_ROLE) == root:
                return row

    def _updateScaleNoteNames(self, root: Note):
        """
        Update the note names based on the scale denoted by the new given root
        note.
        """
        assert isinstance(root, Note)
        maj_scale = scales.MajorScale(root)
        notes = maj_scale.scale()
        note_names = [note.value for note in notes]
        self._scale_note_names.setStringList(note_names)


if __name__ == '__main__':

    def pure_qml():
        """
        Run QML without any QWidgets.
        """

        # Set up the application window
        app = QGuiApplication(sys.argv)
        view = QQuickView()
        view.setResizeMode(QQuickView.SizeRootObjectToView)

        # Expose the manager to the Qml code
        manager = Manager()
        view.rootContext().setContextProperty("manager", manager)

        # Load the QML file
        qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
        print(qml_file)
        view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

        # Show the window
        if view.status() == QQuickView.Error:
            sys.exit(-1)
        view.show()

        # Execute and cleanup
        app.exec_()
        del view

    def mix():
        """
        Run QML inside a QWidget.
        """
        # Set up the application window
        app = QApplication(sys.argv)
        window = QWidget()

        # To use a QML view we need this widget
        qquick_widget = QQuickWidget()
        qquick_widget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)

        # Expose the manager to the Qml code
        manager = Manager()
        qquick_widget.rootContext().setContextProperty("manager", manager)

        # Load the QML file
        qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
        qquick_widget.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

        # Allow QML to take up the full window
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(qquick_widget)
        window.setLayout(layout)

        window.show()
        app.exec_()

    mix()




