import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from gamepad import Gamepad


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.gamepad = Gamepad("/dev/ACM0")

        self.widgetLayout = QtWidgets.QVBoxLayout(self)

        self.portLabel = QtWidgets.QLabel("Arduino Port: ", self)
        self.portInput = QtWidgets.QLineEdit(self)
        self.portInput.setText("/dev/ACM0")
        self.portLayout = QtWidgets.QHBoxLayout()
        self.widgetLayout.addLayout(self.portLayout)

        self.portLayout.addWidget(self.portLabel)
        self.portLayout.addWidget(self.portInput)

        self.createBindField()

    def createBindField(self):
        for k, v in self.gamepad.joystick.joystick.items():
            self.bindLabel = QtWidgets.QLabel(k, self)
            self.bindInput = QtWidgets.QLineEdit(self)
            self.bindInput.setText(v["bind"])
            self.bindLayout = QtWidgets.QHBoxLayout()
            self.widgetLayout.addLayout(self.bindLayout)

            self.bindLayout.addWidget(self.bindLabel)
            self.bindLayout.addWidget(self.bindInput)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
