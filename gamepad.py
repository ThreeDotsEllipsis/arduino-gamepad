import pyautogui
import serial


class Joystick:
    joystick = {
        "y_up": {"bind": "w", "pulled": False},
        "y_down": {"bind": "s", "pulled": False},
        "x_left": {"bind": "a", "pulled": False},
        "x_right": {"bind": "d", "pulled": False},
    }

    def pull(self, input):
        self.joystick[input]["pulled"] = True
        pyautogui.keyDown(self.joystick[input]["bind"])

    def release(self, input):
        self.joystick[input]["pulled"] = False
        pyautogui.keyUp(self.joystick[input]["bind"])

    def handle_joystick(self, input):
        match input:
            case b"s":
                self.pull("y_down")

            case b"w":
                self.pull("y_up")

            case b"ye":
                if self.joystick["y_down"]["pulled"]:
                    self.release("y_down")
                if self.joystick["y_up"]["pulled"]:
                    self.release("y_up")

            case b"a":
                self.pull("x_left")

            case b"d":
                self.pull("x_right")

            case b"xe":
                if self.joystick["x_left"]["pulled"]:
                    self.release("x_left")
                if self.joystick["x_right"]["pulled"]:
                    self.release("x_right")


class Buttons:
    buttons = {
        "a": {"bind": "e", "pressed": False},
        "b": {"bind": "shift", "pressed": False},
        "x": {"bind": "q", "pressed": False},
        "y": {"bind": "c", "pressed": False},
        "down": {"bind": "f1", "pressed": False},
        "left": {"bind": "f", "pressed": False},
    }

    def press(self, button):
        pyautogui.keyDown(self.buttons[button]["bind"])
        self.buttons[button]["pressed"] = True

    def handle_buttons(self, input):
        match input:
            case b"905" | b"906":
                self.press("x")

            case b"674" | b"675":
                self.press("b")

            case b"560" | b"561":
                self.press("y")

            case b"789" | b"790":
                self.press("a")

            case b"335" | b"336":
                self.press("down")

            case b"447" | b"448":
                self.press("left")

            case b"be":
                for v in self.buttons.values():
                    if v["pressed"]:
                        pyautogui.keyUp(v["bind"])
                        v["pressed"] = False


class Gamepad:
    def __init__(self, port):
        # self.arduino = serial.Serial(port=port, baudrate=9600, timeout=0.1)
        self.joystick = Joystick()
        self.button_handler = Buttons()

    def keybind_joystick(self, axis, bind):
        self.joystick.joystick[axis]["bind"] = bind

    def keybind_buttons(self, button, bind):
        self.button_handler.buttons[button]["bind"] = bind

    def run(self):
        while True:
            # data = self.arduino.readline()
            data = ""

            self.button_handler.handle_buttons(data.strip())
            self.joystick.handle_joystick(data.strip())
