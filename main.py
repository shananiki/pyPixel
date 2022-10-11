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


rock1 = (220, 46, 289, 113)
rock2 = (110, 163, 163, 225)
rock3 = (223, 263, 287, 326)
#m.bez_w(10, 10)


clr1_pos = (273, 93)
clr1 = (93, 49, 38)

clr2_pos = (137, 176)
clr2 = (81, 45, 35)

clr3_pos = (240, 276)
clr3 = (78, 43, 33)

inv = Inventory(window_grabber, m, w)
for i in range(0, 50000):
    if inv.isInventoryFull():
        inv.drop_all()
    else:
        m.moveToSquare_r(rock1)
        sleep_s()
        m.left()
        sleep_s()
        window_grabber.sleepUntilColor(clr1_pos, clr1)
        if inv.isInventoryFull():
            inv.drop_all()
        sleep_s()
        m.moveToSquare_r(rock2)
        sleep_s()
        m.left()
        window_grabber.sleepUntilColor(clr2_pos, clr2)
        if inv.isInventoryFull():
            inv.drop_all()
        sleep_s()
        m.moveToSquare_r(rock3)
        sleep_s()
        m.left()
        window_grabber.sleepUntilColor(clr3_pos, clr3)
        if inv.isInventoryFull():
            inv.drop_all()
        sleep_s()
        m.left()


long_wait_counter = 30

# for i in range(0, 50000):
#     full = inv.isInventoryFull()
#     if full:
#         inv.drop_all()
#     else:
#         sleep_s()
#         m.moveToSquare_r(rock1)
#         m.left()


# for i in range(0, 1200):
#     long_wait = False
#     long_wait_counter = long_wait_counter - 1
#     if long_wait_counter == 2:
#         rnd(2000, 3500)
#         long_wait_counter = random.randint(10, 30)
#     else:
#         rnd(400, 800)
#     m.moveToSquare_r((665, 262, 679, 276))
#     rnd(40, 400)
#     m.left()
#     rnd(250, 500)
#     m.moveToSquare_r((390, 195, 421, 235))
#     rnd(250, 500)
#     m.left()
