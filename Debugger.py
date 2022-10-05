from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from pynput import keyboard
from Core import *
from Interfaces import *
from Inventory import *


with open('user.txt') as f:
    lines = f.readlines()
    window_name = lines[0]

COMBINATIONS = [
    {keyboard.KeyCode(char='d')},
    {keyboard.KeyCode(char='D')}
]

# The currently active modifiers
current = set()

def execute():
    window_handle = FindWindow(None, window_name)
    window_rect = GetWindowRect(window_handle)
    w = Window(window_handle)
    window_grabber = WindowGrabber(w)


    mouse = Mouse(w)
    mouse_pos_in_window = w.getMouseInWindow()

    i = Interfaces(window_grabber, mouse, w)
    #i.openInventory()
    inv = Inventory(window_grabber, mouse, w)
    #inv.drop_item(5)

    #
    print("Mouse Position in Window: {0}".format(mouse_pos_in_window))
    print("Color at Mouse Position: {0}".format(window_grabber.getPixel(mouse_pos_in_window)))
    #
    # print("Looking for Pixel (30, 30, 30)")
    # find_pos = window_grabber.findPixel((10, 87, 347))
    # dest_pos = window_grabber.findPixel((154, 120, 27))
    # print("Found Pixel (30, 30, 30) at: {0}".format(window_grabber.findPixel((154, 120, 27))))
    # mouse.bez(dest_pos[0], dest_pos[1])


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
