from win32gui import *
from win32api import *
from win32com import *
from win32con import *
import time
import beziers
import random

###
import numpy as np
from scipy import interpolate
import math


class Mouse:

    def __init__(self):
        self.pos_x = GetCursorPos()[0]
        self.pos_y = GetCursorPos()[1]

    def getMousePos(self):
        return (GetCursorPos()[0], GetCursorPos()[1])

    def moveTo(self, x, y):
        SetCursorPos((x, y))

    def left(self):
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)

    def right(self):
        mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(.1)
        mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0)

    def point_dist(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def moveToSquare(self, x, y, x2, y2):
        random_x = random.randint(x, x2)
        random_y = random.randint(y, y2)
        self.bez(random_x, random_y)

    def bez(self, x2, y2):
        cp = 3
        start = GetCursorPos()
        x1 = start[0]
        y1 = start[1]

        # Distribute control points between start and destination evenly.
        x = np.linspace(x1, x2, num=cp, dtype='int')
        y = np.linspace(y1, y2, num=cp, dtype='int')

        # Randomise inner points a bit (+-RND at most).
        RND = 20
        xr = [random.randint(-RND, RND) for k in range(cp)]
        yr = [random.randint(-RND, RND) for k in range(cp)]
        xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        x += xr
        y += yr

        # Approximate using Bezier spline.
        degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
        # Must be less than number of control points.
        tck, u = interpolate.splprep([x, y], k=degree)
        # Move upto a certain number of points
        u = np.linspace(0, 1, num=2 + int(self.point_dist(x1, y1, x2, y2) / 50.0))
        points = interpolate.splev(u, tck)

        # Move mouse.
        duration = 0.1
        timeout = duration / len(points[0])
        point_list = zip(*(i.astype(int) for i in points))
        for point in point_list:
            SetCursorPos(point)
            time.sleep(timeout + random.randint(20, 40)/1000)