import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from gamepad import Gamepad


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.gamepad = Gamepad("/dev/ACM0")
        self.widgetLayout = QtWidgets.QVBoxLayout(self)

        self.createInput("Arduino Port: ", "/dev/ACM0")

        self.joystickLayout = QtWidgets.QVBoxLayout()
        self.buttonLayout = QtWidgets.QVBoxLayout()
        self.bindLayout = QtWidgets.QHBoxLayout()

        for k, v in self.gamepad.joystick.joystick.items():
            self.createInput(k, v["bind"], self.joystickLayout)

        for k, v in self.gamepad.button_handler.buttons.items():
            self.createInput(k, v["bind"], self.buttonLayout)

        self.bindLayout.addLayout(self.joystickLayout)
        self.bindLayout.addLayout(self.buttonLayout)
        self.widgetLayout.addLayout(self.bindLayout)

        self.runButton = QtWidgets.QPushButton("Run")
        self.widgetLayout.addWidget(self.runButton)

    def createInput(self, text, defaultInput="", parent=None):
        if parent == None:
            parent = self.widgetLayout

        label = QtWidgets.QLabel(text, self)
        input = QtWidgets.QLineEdit(self)
        input.setText(defaultInput)
        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(label)
        layout.addWidget(input)

        parent.addLayout(layout)

        return input


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
