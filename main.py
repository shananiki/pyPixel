from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from Core import *
from Inventory import *

#Uncomment, just hiding my Windowname
with open('user.txt') as f:
    lines = f.readlines()
    window_name = lines[0]

window_handle = FindWindow(None, window_name)


w = Window(window_handle)



window_grabber = WindowGrabber(w)
window_grabber.screenshot()

m = Mouse(w)

locker = (344, 150, 401, 231)
paste = (573, 284, 586, 301)
floor = (235, 178, 256, 205)
paste_in_locker = (410, 265, 432, 292)

square_spell = (664, 261, 675, 275)
square_enemy = (379, 193, 406, 231)

long_wait_counter = 10
second_wait = 10

bank = (1024, 387, 1157, 602)
bank_all = (891, 729, 921, 763)
item_1 = (725, 453, 751, 479)
close_bank = (963, 40, 979, 60)
inv_item_1 = (1350, 606, 1371, 628)
inv_item_2 = (1411, 607, 1444, 635)
make_all = (504, 865, 570, 954)

for i in range(0, 40):
    m.moveToSquare_r(bank)
    rnd(40, 80)
    m.left()
    rnd(1200, 1800)
    m.moveToSquare_r(bank_all)
    rnd(40, 80)
    m.left()
    m.moveToSquare_r(item_1)
    rnd(40, 80)
    m.left()
    m.moveToSquare_r(close_bank)
    rnd(40, 80)
    m.left()
    rnd(500, 1000)
    m.moveToSquare_r(inv_item_1)
    rnd(40, 80)
    m.left()
    m.moveToSquare_r(inv_item_2)
    rnd(40, 80)
    m.left()
    rnd(400, 800)
    m.moveToSquare_r(make_all)
    rnd(40, 80)
    m.left()
    rnd(39000, 44000)





