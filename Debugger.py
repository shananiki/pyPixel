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
    {keyboard.KeyCode(char='D')},
    {keyboard.KeyCode(char='S')},
    {keyboard.KeyCode(char='s')},
    {keyboard.KeyCode(char='e')},
    {keyboard.KeyCode(char='E')}
]

# The currently active modifiers
current = set()
running = None
def execute():
    window_handle = FindWindow(None, window_name)
    window_rect = GetWindowRect(window_handle)
    w = Window(window_handle)
    window_grabber = WindowGrabber(w)


    mouse = Mouse(w)
    mouse_pos_in_window = w.getMouseInWindow()

    #
    print("Mouse Position in Window: {0}".format(mouse_pos_in_window))
    #
    # print("Looking for Pixel (30, 30, 30)")
    # find_pos = window_grabber.findPixel((10, 87, 347))
    # dest_pos = window_grabber.findPixel((154, 120, 27))
    # print("Found Pixel (30, 30, 30) at: {0}".format(window_grabber.findPixel((154, 120, 27))))
    # mouse.bez(dest_pos[0], dest_pos[1])


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        print(key)
        if key == keyboard.KeyCode(char='d'):
            execute()
        if key == keyboard.KeyCode(char='e'):
            stop()
        if key == keyboard.KeyCode(char='s'):
            start()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
def stop():
    print("Stop")
    running = False
    sys.exit(1)

def start():
    print("Start")
    running = True
    while running:
        mouse.moveToSquare_r((1568, 741, 1568, 741))
        sleep_s()
        mouse.moveToSquare_r((1268, 741, 1268, 741))


window_handle = FindWindow(None, window_name)
window_rect = GetWindowRect(window_handle)
w = Window(window_handle)
window_grabber = WindowGrabber(w)


mouse = Mouse(w)
mouse_pos_in_window = w.getMouseInWindow()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
