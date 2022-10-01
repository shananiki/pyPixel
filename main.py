from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *
from Core import *

#Uncomment, just hiding my Windowname
with open('user.txt') as f:
    lines = f.readlines()
    window_name = lines[0]

window_handle = FindWindow(None, window_name)


w = Window(window_handle)



#
#window_grabber = WindowGrabber(window_handle)
#window_grabber.screenshot()
#window_grabber.getPixel(10, 10)

m = Mouse()

long_wait_counter = 30

for i in range(0, 300):
    long_wait = False
    long_wait_counter = long_wait_counter - 1
    if long_wait_counter == 2:
        rnd(2000, 3500)
        long_wait_counter = random.randint(10, 30)
    else:
        rnd(400, 800)
    m.bez(random.randint(669, 680), random.randint(264, 277))
    rnd(40, 400)
    m.left()
    rnd(60, 180)
    m.bez(random.randint(498, 515), random.randint(271, 297))
    rnd(60, 500)
    m.left()
