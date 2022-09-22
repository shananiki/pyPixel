from win32gui import *
from win32gui import SetCursor
from win32api import *
from Mouse import *

window_handle = FindWindow(None, "oko2k.txt - Editor")
window_rect   = GetWindowRect(window_handle)

print(GetCursorPos())


m = Mouse()
m.bezier((200, 200))
m.left()