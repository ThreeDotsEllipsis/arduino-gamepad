from sys import pycache_prefix
import pyautogui
import serial
import time

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=0.1)


w_press = False
s_press = False
a_press = False
d_press = False

while True:
    data = arduino.readline()

    if data.strip() == b"905" or data.strip() == b"906":
        pyautogui.keyDown("q")
        time.sleep(0.1)
    elif data.strip() == b"674" or data.strip() == b"675":
        pyautogui.keyDown("shift")
        time.sleep(0.1)
    elif data.strip() == b"560" or data.strip() == b"561":
        pyautogui.keyDown("c")
        time.sleep(0.1)
    elif data.strip() == b"789" or data.strip() == b"790":
        pyautogui.keyDown("e")
        time.sleep(0.1)
    elif data.strip() == b"335" or data.strip() == b"336":
        pyautogui.keyDown("f1")
        time.sleep(0.1)
    elif data.strip() == b"447" or data.strip() == b"448":
        pyautogui.keyDown("f")
        time.sleep(0.1)
    elif data.strip() == b"be":
        pyautogui.keyUp("f1")
        pyautogui.keyUp("q")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("c")
        pyautogui.keyUp("e")
        pyautogui.keyUp("f")

    if data.strip() == b"s":
        s_press = True
        pyautogui.keyDown("s")
        time.sleep(0.1)
    elif data.strip() == b"w":
        w_press = True
        pyautogui.keyDown("w")
        time.sleep(0.1)
    elif data.strip() == b"ye":
        if s_press:
            s_press = False
            pyautogui.keyUp("s")
        if w_press:
            w_press = False
            pyautogui.keyUp("w")

    if data.strip() == b"a":
        a_press = True
        pyautogui.keyDown("a")
        time.sleep(0.1)
    elif data.strip() == b"d":
        d_press = True
        pyautogui.keyDown("d")
        time.sleep(0.1)
    elif data.strip() == b"xe":
        if d_press:
            d_press = False
            pyautogui.keyUp("d")
        if a_press:
            a_press = False
            pyautogui.keyUp("a")
