import os
import sys

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtQuickWidgets import QQuickWidget

from src.main import Manager


def main():
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
    qml_file = os.path.join(os.path.dirname(__file__), "src/main.qml")
    qquick_widget.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

    # Allow QML to take up the full window
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(qquick_widget)
    window.setLayout(layout)

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
