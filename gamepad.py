from sys import pycache_prefix
import pyautogui
import serial

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=0.1)


class Joystick:
    y_up_pull = False
    y_down_pull = False
    x_left_pull = False
    x_right_pull = False

    y_up = "w"
    y_down = "s"
    x_left = "a"
    x_right = "d"

    def handle_joystick(self, input):
        match input:
            case b"s":
                self.y_down_pull = True
                pyautogui.keyDown(self.y_down)

            case b"w":
                self.y_up_pull = True
                pyautogui.keyDown(self.y_up)

            case b"ye":
                if self.y_down_pull:
                    self.y_down_pull = False
                    pyautogui.keyUp(self.y_down)
                if self.y_up_pull:
                    self.y_up_pull = False
                    pyautogui.keyUp(self.y_up)

            case b"a":
                self.x_left_pull = True
                pyautogui.keyDown(self.x_left)

            case b"d":
                self.x_right_pull = True
                pyautogui.keyDown(self.x_right)

            case b"xe":
                if self.x_right_pull:
                    self.x_right_pull = False
                    pyautogui.keyUp(self.x_right)
                if self.x_left_pull:
                    self.x_left_pull = False
                    pyautogui.keyUp(self.x_left)


class Buttons:
    buttons = {
        "a": {"bind": "e", "pressed": False},
        "b": {"bind": "shift", "pressed": False},
        "x": {"bind": "q", "pressed": False},
        "y": {"bind": "c", "pressed": False},
        "down": {"bind": "f", "pressed": False},
        "left": {"bind": "f1", "pressed": False},
    }

    def press(self, button):
        pyautogui.keyDown(self.buttons[button]["bind"])
        self.buttons[button]["pressed"] = True

    def handle_buttons(self, input):
        match input:
            case [b"905", b"906"]:
                self.press("x")

            case [b"674", b"675"]:
                self.press("b")

            case [b"560", b"561"]:
                self.press("y")

            case [b"789", b"790"]:
                self.press("a")

            case [b"335", b"336"]:
                self.press("down")

            case [b"447", b"448"]:
                self.press("left")

            case [b"be"]:
                for k, v in self.buttons.items():
                    if v["pressed"]:
                        pyautogui.keyUp(k)
                        v["pressed"] = False


joystick = Joystick()
button_handler = Buttons()

while True:
    data = arduino.readline()

    button_handler.handle_buttons(data.strip())
    joystick.handle_joystick(data.strip())
