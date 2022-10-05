from win32gui import *
from PIL import ImageGrab
from Window import *

class RGB:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class WindowGrabber:

    def __init__(self, window):
        self.image = None
        self.window = window
        self.window_hwnd = window.getHwnd()

    def screenshot(self):
        SetForegroundWindow(self.window_hwnd)
        dimensions = GetWindowRect(self.window_hwnd)
        self.image = ImageGrab.grab(dimensions)
        return self.image

    def getPixel(self, pos, type=""):
        if self.image == None:
            self.screenshot()
        if type == "RGB":
            return RGB()
        else:
            return self.image.getpixel(pos)

    def isColorAt(self, pos, RGB):
        if self.image == None:
            self.screenshot()
        pixel = self.image.getpixel((pos[0], pos[1]))
        if (pixel[0] == RGB[0]) and (pixel[1] == RGB[1]) and (pixel[2] == RGB[2]):
            return True
        else:
            return False

    def findPixel(self, RGB):
        if self.image == None:
            self.screenshot()

        x = self.image.size[0]
        y = self.image.size[1]
        for x in range(0, x):
            for y in range(0, y):
                pixel = self.image.getpixel((x, y))
                if (pixel[0] == RGB[0]) and (pixel[1] == RGB[1]) and (pixel[2] == RGB[2]):
                    return (x, y)
        return "Not found"