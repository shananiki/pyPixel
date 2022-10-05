from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from Core import *


class Inventory:

    def __init__(self, wg, m, w):
        self.window_grabber = wg
        self.mouse = m
        self.window = w
        self.INVENTORY_POS = [
            [575, 245, 591, 266],
            [614, 245, 633, 266],
            [656, 245, 675, 266],
            [700, 245, 719, 266],
            [575, 282, 593, 304],
            [614, 281, 633, 304],
            [656, 282, 677, 304],
            [699, 281, 718, 304]
        ]
    
    def drop_item(self, n):
        n = n - 1
        self.mouse.moveToSquare_r(self.INVENTORY_POS[n])