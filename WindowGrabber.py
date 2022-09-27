from win32gui import *
from PIL import ImageGrab

class WindowGrabber:


    def __init__(self, hwnd):
        self.window_hwnd = hwnd
        self.image = None

    def screenshot(self):
        SetForegroundWindow(self.window_hwnd)
        dimensions = GetWindowRect(self.window_hwnd)
        self.image = ImageGrab.grab(dimensions)
        return self.image

    def getPixel(self, x, y):
        if not self.image == None:
            print(self.image.getpixel((x, y)))
            return (x, y)
