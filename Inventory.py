from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from Core import *


class Inventory:

    def __init__(self, wg: WindowGrabber, m: Mouse, w: Window):
        self.window_grabber = wg
        self.mouse = m
        self.window = w
        self.INVENTORY_POS = [
            (575, 245, 591, 266),
            (614, 245, 633, 266),
            (656, 245, 675, 266),
            (700, 245, 719, 266),
            (575, 282, 593, 304),
            (614, 281, 633, 304),
            (656, 282, 677, 304),
            (699, 281, 718, 304),
            (573, 321, 587, 337),
            (616, 322, 630, 335),
            (659, 320, 673, 338),
            (699, 320, 713, 336),
            (573, 357, 589, 373),
            (616, 356, 629, 373),
            (658, 357, 671, 372),
            (702, 357, 714, 372),
            (573, 392, 589, 407),
            (618, 392, 630, 408),
            (659, 393, 673, 408),
            (700, 394, 716, 410),
            (574, 430, 588, 445),
            (618, 430, 632, 446),
            (658, 430, 674, 445),
            (698, 431, 716, 446),
            (573, 465, 588, 482),
            (615, 464, 630, 480),
            (658, 465, 672, 480),
            (699, 465, 715, 481)
        ]

    def isInventoryFull(self):
        poss = (708, 472)
        clr = (75, 66, 58)
        poss2 = (713, 477)
        clr2 = (73, 64, 53)
        if not self.window_grabber.isColorAt(poss, clr) or not self.window_grabber.isColorAt(poss2, clr2):
            return True
        else:
            return False

    def drop_all(self):
        for i in range(0, 28):
            self.drop_item(i)
            sleep_s()
            self.mouse.left()
            sleep_s()
        rnd_slp = random.randint(1000, 4000) / 1000
        print("Sleeping for {0}".format(rnd_slp))
        time.sleep(rnd_slp)

    def drop_all_except(self, exceptions: tuple[int, ...]):
        for i in range(0, 27):
            if i in exceptions:
                continue
            else:
                self.drop_item(self, i)
                sleep_s()
                self.mouse.left()
                sleep_s()
    
    def drop_item(self, n: int):
        self.mouse.moveToSquare_r(self.INVENTORY_POS[n])