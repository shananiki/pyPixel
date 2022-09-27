from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *
from Window import *
from WindowGrabber import *

window_handle = FindWindow(None, "RuneLite")
window_rect   = GetWindowRect(window_handle)
print("Windows rect: {0}".format(window_rect))
print(GetCursorPos())


w = Window(window_rect[0], window_rect[1], window_rect[2], window_rect[3])

window_grabber = WindowGrabber(window_handle)
window_grabber.screenshot()
window_grabber.getPixel(10, 10)

#m = Mouse()
#m.bezier((200, 200))
#m.left()