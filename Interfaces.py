from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from Core import *


class Interfaces:

    def __init__(self, wg, m, w):
        self.window_grabber = wg
        self.mouse = m
        self.window = w
        self.INVENTORY_POS = [634, 199, 655, 225]

    def openInventory(self):
        if self.isInventoryOpen() == False:
            self.mouse.moveToSquare_r(self.INVENTORY_POS)
            sleep_s()
            self.mouse.left()

    def isInventoryOpen(self):
        self.window_grabber.screenshot()
        pixel = self.window_grabber.getPixel((635, 200))
        if (pixel[0] == 113) and (pixel[1] == 38) and (pixel[2] == 29):
            print("Inventory is open!")
            return True
        else:
            print("Inventory is closed!")
            return False