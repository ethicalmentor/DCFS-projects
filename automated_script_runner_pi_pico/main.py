import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(3)

#if not 'network.txt' in os.listdir():
#    time.sleep(1.5)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(1.0)
layout.write("cmd\n")
time.sleep(1.0)

#    layout.write("e:\n")
#    time.sleep(0.05)

layout.write("notepad.exe\n")
time.sleep(1.0)

#    keyboard.send(Keycode.ALT, Keycode.F4)
