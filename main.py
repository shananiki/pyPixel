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



#m.bez_w(10, 10)

long_wait_counter = 30
inv = Inventory(window_grabber, m, w)
for i in range(0, 50000):
    full = inv.isInventoryFull()
    if full:
        inv.drop_all()
    else:
        sleep_s()
        if not m.inArea((330, 175, 404, 250)):
            m.moveToSquare_r((330, 175, 404, 250))
            m.left()
        else:
            sleep_s()
            m.left()


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
