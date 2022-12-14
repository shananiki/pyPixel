
from win32gui import *
from win32gui import SetCursor
from win32api import *

from Mouse import *


class Window:

    def __init__(self, window_handle):
        self.window_handle = window_handle
        self.window_rect = GetWindowRect(self.window_handle)
        self.x = self.window_rect[0]
        self.y = self.window_rect[1]
        self.w = self.window_rect[2]
        self.h = self.window_rect[3]
        from win32api import GetSystemMetrics
        self.screen_w = GetSystemMetrics(0)
        self.screen_h = GetSystemMetrics(1)

    def updateWindowPos(self):
        self.window_rect = GetWindowRect(self.window_handle)
        self.x = self.window_rect[0]
        self.y = self.window_rect[1]
        self.w = self.window_rect[2]
        self.h = self.window_rect[3]

    def getHwnd(self):
        return self.window_handle

    def getMouseInWindow(self):
        mouse_pos = GetCursorPos()[0], GetCursorPos()[1]
        mouse_in_window_x = mouse_pos[0] - self.x
        mouse_in_window_y = mouse_pos[1] - self.y
        return (mouse_in_window_x, mouse_in_window_y)

    def printWindowPos(self):
        print(self.x, self.y, self.w, self.h)

    def printScreenSize(self):
        print("Width =", self.screen_w)
        print("Height =", self.screen_h)

    def getScreenWidth(self):
        return self.screen_w

    def getScreenHeight(self):
        return self.screen_h

    def getWindowRect(self):
        return self.window_rect

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h