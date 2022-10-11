from win32gui import *
from PIL import ImageGrab
from Window import *


class RGB:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class WindowGrabber:

    def __init__(self, window: Window):
        self.image = None
        self.window = window
        self.window_hwnd = window.getHwnd()

    def screenshot(self):
        SetForegroundWindow(self.window_hwnd)
        dimensions = GetWindowRect(self.window_hwnd)
        self.image = ImageGrab.grab(dimensions)
        return self.image

    def getPixel(self, pos: tuple[int, int], mode: str = ""):
        if self.image is None:
            self.screenshot()
        if mode == "RGB":
            return RGB()
        else:
            return self.image.getpixel(pos)

    def isColorAt(self, pos: tuple[int, int], rgb: tuple[int, ...]):
        self.screenshot()
        pixel = self.image.getpixel((pos[0], pos[1]))
        print("Looking for {0} at {1}".format(rgb, pos))
        print("Found Pixel {0} at {1}".format(pixel, pos))
        if (pixel[0] == rgb[0]) and (pixel[1] == rgb[1]) and (pixel[2] == rgb[2]):
            return True
        else:
            return False

    def sleepUntilColor(self, pos, rgb):
        while self.isColorAt(pos, rgb):
            time.sleep(1)

    def findPixel(self, rgb: tuple[int, ...]):
        if self.image is None:
            self.screenshot()

        x = self.image.size[0]
        y = self.image.size[1]
        for x in range(0, x):
            for y in range(0, y):
                pixel = self.image.getpixel((x, y))
                if (pixel[0] == rgb[0]) and (pixel[1] == rgb[1]) and (pixel[2] == rgb[2]):
                    return (x, y)
        return "Not found"
